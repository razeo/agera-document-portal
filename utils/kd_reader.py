"""
KD 2025 Reader — search and validate KD codes from the official MONSTAT database.

Loads the JSON file generated from the KD 2025 PDF source and provides:
- Fast search by code or name
- Sector filtering
- Code validation and full description resolution
- Semantic / natural language search with domain keyword taxonomy
"""
import json
import os
import re
from pathlib import Path
from typing import Optional

# Default path to the KD 2025 JSON
DEFAULT_KD_PATH = os.path.join(
    os.path.expanduser('~'), 'agera-knowledge', 'processed', 'kd-2025-djelatnosti.json'
)

# ─── Domain Keyword Taxonomy ──────────────────────────────────────────────────
#
# Maps broad industry terms (what a user might type naturally) to:
#   terms:         Phrases that trigger this domain match
#   rel_terms:     Keywords to search in names and descriptions
#   sectors:       All KD codes from these sectors are included (broad match)
#   code_prefixes: Optional code prefix filters for refinement
#   label:         Human-readable label (falls back to key name)
#
DOMAIN_MAP = {
    'turizam': {
        'label': 'Turizam',
        'terms': ['turizam', 'turistički', 'turistička', 'turizma', 'travel',
                  'tourism', 'putovanja', 'izleti', 'turist'],
        'rel_terms': ['hotel', 'smještaj', 'apartman', 'kamp', 'odmaralište',
                      'putnička agencija', 'turoperator', 'rezervacija', 'izlet',
                      'nacionalni park', 'turistička'],
        'sectors': ['I', 'N'],
        'code_prefixes': ['55.', '56.', '79.1', '79.9'],
    },
    'ugostiteljstvo': {
        'label': 'Ugostiteljstvo',
        'terms': ['ugostiteljstvo', 'ugostitelj', 'ugostiteljska', 'ugostiteljski',
                  'restoran', 'catering', 'ketering', 'bar', 'kafić', 'kafana',
                  'hrana i piće', 'posluživanje hrane'],
        'rel_terms': ['restoran', 'bar', 'kafić', 'catering', 'hrana', 'piće',
                      'posluživanje', 'ketering', 'menza', 'kuhanje', 'kuhinja',
                      'ugostitelj'],
        'sectors': ['I'],
        'code_prefixes': ['56.'],
    },
    'trgovina': {
        'label': 'Trgovina',
        'terms': ['trgovina', 'trgovinski', 'trgovački', 'trgovačka', 'prodaja',
                  'trade', 'commerce', 'wholesale', 'retail', 'veleprodaja',
                  'maloprodaja', 'trgovina na veliko', 'trgovina na malo',
                  'kupoprodaja', 'prodavnica'],
        'rel_terms': ['prodaja', 'veleprodaja', 'maloprodaja', 'prodavnica',
                      'market', 'tržni', 'trgov', 'trgovina', 'kupoprodaja'],
        'sectors': ['G'],
        'code_prefixes': ['46.', '47.'],
    },
    'građevinarstvo': {
        'label': 'Građevinarstvo',
        'terms': ['građevinarstvo', 'građevina', 'građevinski', 'građevinska',
                  'građevinske', 'gradnja', 'izgradnja', 'gradevina', 'gradevinski',
                  'construction', 'building', 'renoviranje', 'adaptacija',
                  'građevinske usluge'],
        'rel_terms': ['gradnja', 'izgradnja', 'građevin', 'gradev', 'renoviranje',
                      'adaptacija', 'sanacija', 'montaža', 'instalacija', 'rušenje',
                      'zidars', 'krov', 'malteris', 'bojenj', 'stolarij', 'fasada',
                      'beton', 'armatura', 'ograd'],
        'sectors': ['E'],
        'code_prefixes': ['41.', '42.', '43.'],
    },
    'poljoprivreda': {
        'label': 'Poljoprivreda, šumarstvo, ribarstvo',
        'terms': ['poljoprivreda', 'poljoprivredni', 'poljoprivredno',
                  'poljoprivredna', 'poljoprivrednik', 'gajenje', 'uzgoj',
                  'ratarstvo', 'stočarstvo', 'voćarstvo', 'vinogradarstvo',
                  'farma', 'agriculture', 'farming', 'zemljoradnja',
                  'šumarstvo', 'ribarstvo'],
        'rel_terms': ['gajenje', 'uzgoj', 'ratarstvo', 'stočarstvo', 'voćarstvo',
                      'vinogradarstvo', 'ribarstvo', 'šumarstvo', 'poljoprivred',
                      'sjem', 'žitaric', 'povrć', 'voć', 'vinograd', 'maslin',
                      'stabl', 'biljak', 'stok'],
        'sectors': ['A'],
        'code_prefixes': ['01.', '02.', '03.'],
    },
    'proizvodnja': {
        'label': 'Prerađivačka industrija (proizvodnja)',
        'terms': ['proizvodnja', 'proizvodni', 'proizvodna', 'proizvođač',
                  'industrija', 'prerađivačka', 'manufacturing', 'production',
                  'fabrika', 'prerađivački', 'manufaktura', 'prerada'],
        'rel_terms': ['proizvodnj', 'fabrika', 'prerađivačk', 'prehramben',
                      'hemijsk', 'metaloprera', 'mašin', 'oprem', 'proizvod',
                      'prehrambeni', 'hemijski', 'metalni', 'drvni', 'tekstil',
                      'odjeća', 'namještaj', 'plastika', 'papir', 'guma'],
        'sectors': ['C'],
        'code_prefixes': [f'{i}.' for i in range(10, 34)],
    },
    'transport': {
        'label': 'Saobraćaj, transport i logistika',
        'terms': ['transport', 'prevoz', 'saobraćaj', 'špedicija', 'logistika',
                  'dostava', 'kurir', 'transportni', 'transportna', 'logistički',
                  'prijevoz', 'transportation', 'logistics', 'shipping', 'delivery',
                  'skladištenje'],
        'rel_terms': ['prevoz', 'transport', 'špedicija', 'logistik', 'skladišt',
                      'dostava', 'kurir', 'putnik', 'teret', 'brod', 'avion',
                      'šleper', 'kamion', 'autobus', 'taksi'],
        'sectors': ['H'],
        'code_prefixes': ['49.', '50.', '51.', '52.', '53.'],
    },
    'it': {
        'label': 'IT, programiranje, računari',
        'terms': ['it', 'informacione tehnologije', 'programiranje', 'softver',
                  'računari', 'računarski', 'informatika', 'informatički',
                  'it usluge', 'web', 'aplikacija', 'programer', 'developer',
                  'sajt', 'software', 'computer', 'programming', 'coding',
                  'telekomunikacije', 'cloud', 'it konsalting'],
        'rel_terms': ['programiranje', 'softver', 'računarsk', 'informatic',
                      'telekom', 'web', 'aplikacij', 'baza podataka',
                      'informacioni', 'hardver', 'konsult', 'cloud', 'mrež',
                      'server', 'telekomunik', 'emitersk', 'izdavačk'],
        'sectors': ['J', 'K'],
        'code_prefixes': ['58.', '59.', '60.', '61.', '62.', '63.'],
    },
    'finansije': {
        'label': 'Finansije, osiguranje, računovodstvo, konsalting',
        'terms': ['finansije', 'finansijski', 'finansijska', 'bankarstvo',
                  'osiguranje', 'računovodstvo', 'knjigovodstvo', 'konsalting',
                  'konsultantske', 'finance', 'accounting', 'insurance',
                  'banking', 'consulting', 'kredit', 'investicije', 'berza',
                  'revizija', 'poreski'],
        'rel_terms': ['finansij', 'bank', 'osiguranj', 'računovodstv',
                      'knjigovodstv', 'kredit', 'investicij', 'računovođa',
                      'konsult', 'revizij', 'poresk', 'berz', 'lizing'],
        'sectors': ['L', 'M'],
        'code_prefixes': ['64.', '65.', '66.', '69.'],
    },
    'obrazovanje': {
        'label': 'Obrazovanje',
        'terms': ['obrazovanje', 'škola', 'fakultet', 'edukacija', 'obuka',
                  'trening', 'kursevi', 'obrazovni', 'obrazovna', 'education',
                  'training', 'school', 'university', 'college', 'kurs',
                  'podučavanje', 'obrazovne usluge'],
        'rel_terms': ['obrazovanj', 'škola', 'fakultet', 'trening', 'obuka',
                      'edukacij', 'kursevi', 'podučavanj', 'nastav', 'učitelj',
                      'profesor', 'predškol', 'obrazov'],
        'sectors': ['Q'],
        'code_prefixes': ['85.'],
    },
    'zdravstvo': {
        'label': 'Zdravstvo i socijalna zaštita',
        'terms': ['zdravstvo', 'zdravstveni', 'zdravstvena', 'bolnica',
                  'ljekar', 'doktor', 'stomatolog', 'apoteka', 'ljekarna',
                  'farmacija', 'socijalna zaštita', 'health', 'medical',
                  'healthcare', 'hospital', 'pharmacy', 'doctor', 'dentist',
                  'medicina', 'njega starih', 'starački dom'],
        'rel_terms': ['zdravstv', 'bolnica', 'ljekar', 'stomatolog', 'apoteka',
                      'socijaln', 'njega', 'medicin', 'farmac', 'doktor',
                      'hitna', 'rehabilit', 'brižn'],
        'sectors': ['R'],
        'code_prefixes': ['86.', '87.', '88.'],
    },
    'nekretnine': {
        'label': 'Poslovanje nekretninama',
        'terms': ['nekretnine', 'nekretnina', 'promet nekretninama',
                  'poslovanje nekretninama', 'real estate', 'property',
                  'stan', 'kuća', 'iznajmljivanje', 'zakup',
                  'upravljanje nekretninama', 'prodaja nekretnina',
                  'agenc za nekretnine'],
        'rel_terms': ['nekretnin', 'stan', 'kuća', 'poslovni prostor',
                      'iznajmljivanj', 'upravljanj', 'zakup',
                      'prodaja nekretnina', 'agenc za nekretnine',
                      'posredovanje'],
        'sectors': ['M'],
        'code_prefixes': ['68.'],
    },
    'usluge': {
        'label': 'Uslužne djelatnosti',
        'terms': ['usluge', 'uslužne', 'uslužni', 'uslužna', 'servis',
                  'održavanje', 'čišćenje', 'frizerski', 'kozmetički',
                  'popravka', 'pranje', 'fotograf', 'pogreb', 'services',
                  'maintenance', 'cleaning', 'repair', 'frizerske usluge',
                  'liječničke usluge', 'uslužne djelatnosti'],
        'rel_terms': ['frizersk', 'kozmetičk', 'popravka', 'čišćenj', 'pranje',
                      'fotograf', 'pogreb', 'servis', 'održavanj', 'uslug',
                      'pranje', 'iznajmljivanj', 'lizing', 'obezbjeđenj',
                      'istraživanj'],
        'sectors': ['M', 'N', 'O', 'S', 'T'],
        'code_prefixes': ['68.', '69.', '70.', '71.', '72.', '73.', '74.',
                          '75.', '77.', '78.', '79.', '80.', '81.', '82.',
                          '95.', '96.'],
    },
    'energetika': {
        'label': 'Energetika, voda, komunalije',
        'terms': ['energetika', 'energija', 'struja', 'električna',
                  'električne', 'elektro', 'gas', 'voda', 'grijanje',
                  'klimatizacija', 'energy', 'electricity', 'water',
                  'power', 'snabdijevanje', 'komunalne', 'otpad'],
        'rel_terms': ['električn', 'gas', 'snabdijevanj', 'par', 'klimatizac',
                      'vod', 'otpadn', 'energet', 'toplot', 'otpad',
                      'kanalizac', 'deponij'],
        'sectors': ['D', 'E'],
        'code_prefixes': ['35.', '36.', '37.', '38.', '39.', '41.', '42.', '43.'],
    },
    'kultura_sport': {
        'label': 'Kultura, sport, umjetnost, zabava',
        'terms': ['kultura', 'sport', 'zabava', 'umjetnost', 'muzej',
                  'biblioteka', 'arhiv', 'pozorište', 'film', 'muzika',
                  'izložba', 'kockanje', 'igre na sreću', 'entertainment',
                  'sports', 'culture', 'art', 'museum', 'theatre',
                  'fitness', 'rekreacija', 'vježba'],
        'rel_terms': ['umjetnost', 'kultur', 'sport', 'zabav', 'muzej',
                      'bibliotek', 'arhiv', 'pozorišt', 'film', 'muzik',
                      'izložb', 'kockanj', 'igre na sreću', 'rekreativ',
                      'fitness', 'vježba', 'sajam', 'klub'],
        'sectors': ['R', 'S'],
        'code_prefixes': ['90.', '91.', '92.', '93.'],
    },
    'javna_uprava': {
        'label': 'Javna uprava, odbrana, socijalno osiguranje',
        'terms': ['javna uprava', 'državna', 'opština', 'lokalna samouprava',
                  'odbrana', 'vojska', 'socijalno osiguranje', 'policija',
                  'public administration', 'government', 'defense', 'državni'],
        'rel_terms': ['uprav', 'odbran', 'socijalno osiguranj', 'javn',
                      'državn', 'opštin', 'poresk', 'carin', 'policij', 'vojn'],
        'sectors': ['P'],
        'code_prefixes': ['84.'],
    },
    'rudarstvo': {
        'label': 'Rudarstvo, vađenje rude i kamena',
        'terms': ['rudarstvo', 'rudnik', 'ruda', 'kamen', 'kamenolom',
                  'vađenje', 'mine', 'mining', 'mineral', 'nafta'],
        'rel_terms': ['rud', 'kamen', 'kamenolom', 'mineral', 'nafta',
                      'gas', 'ugalj', 'metaličn', 'tres'],
        'sectors': ['B'],
        'code_prefixes': ['05.', '06.', '07.', '08.', '09.'],
    },
}


class KDReader:
    """KD 2025 classification reader with in-memory search index."""

    def __init__(self, json_path: str | None = None):
        self.json_path = json_path or DEFAULT_KD_PATH
        self._codes: list[dict] = []
        self._sectors: list[dict] = []
        self._code_index: dict[str, dict] = {}  # code -> entry
        self._loaded = False

    def _ensure_loaded(self):
        if not self._loaded:
            self._load()

    def _load(self):
        path = Path(self.json_path)
        if not path.exists():
            raise FileNotFoundError(f"KD 2025 database not found: {self.json_path}")

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self._codes = data
        self._code_index = {}

        sectors_seen = {}
        for entry in data:
            code = entry.get('code', '')
            self._code_index[code] = entry

            # Collect sectors
            sec = entry.get('sector', {})
            sec_code = sec.get('code')
            if sec_code and sec_code not in sectors_seen:
                sectors_seen[sec_code] = {
                    'code': sec_code,
                    'name': sec.get('name', ''),
                    'count': 0,
                }
            if sec_code:
                sectors_seen[sec_code]['count'] = sectors_seen[sec_code].get('count', 0) + 1

        self._sectors = sorted(sectors_seen.values(), key=lambda s: s['code'])

        # Sort codes naturally by code string
        self._codes.sort(key=lambda x: x.get('code', ''))
        self._loaded = True

    # ─── Search ───────────────────────────────────────────────────────────────

    def search(self, query: str, limit: int = 20, sector: str | None = None) -> list[dict]:
        """Search KD codes by code or name.

        Args:
            query: Search string (matches code prefix or name substring)
            limit: Max results (default 20)
            sector: Optional sector code filter (e.g. 'A', 'G', 'I')

        Returns:
            List of matching entries with code, name, sector, description
        """
        self._ensure_loaded()
        if not query or len(query) < 1:
            return self._list_all(limit, sector)

        query_lower = query.lower().strip()

        results: list[dict] = []
        seen_codes = set()

        # 1. Code prefix match (highest priority)
        for entry in self._codes:
            code = entry.get('code', '')
            if sector and entry.get('sector', {}).get('code') != sector:
                continue
            if code.startswith(query_lower):
                if code not in seen_codes:
                    seen_codes.add(code)
                    results.append(self._format_result(entry, 'code_prefix'))

        # 2. Code contains match
        for entry in self._codes:
            code = entry.get('code', '')
            if sector and entry.get('sector', {}).get('code') != sector:
                continue
            if query_lower in code and code not in seen_codes:
                seen_codes.add(code)
                results.append(self._format_result(entry, 'code_contains'))

        # 3. Name contains match (lower priority)
        for entry in self._codes:
            code = entry.get('code', '')
            if sector and entry.get('sector', {}).get('code') != sector:
                continue
            if query_lower in entry.get('name', '').lower() and code not in seen_codes:
                seen_codes.add(code)
                results.append(self._format_result(entry, 'name_contains'))

        return results[:limit]

    def semantic_search(self, query: str, limit: int = 200) -> dict:
        """Natural language / semantic search for KD codes.

        Instead of simple substring matching, this method:
        1. Splits query into terms (by comma, semicolon, newline)
        2. Checks each term against the domain keyword taxonomy (e.g. 'turizam' → hotel,
           smještaj, travel agency codes)
        3. For matched domains: returns codes matching the domain's code prefixes
           (focused, not entire sectors)
        4. For unmatched terms: keyword search in code names
        5. Groups results by sector for easier browsing

        Args:
            query: Natural language, e.g. "Turizam, ugostiteljstvo, trgovina"
            limit: Max total results (default 200)

        Returns:
            dict with total, groups (by sector), matched_domains, all_items
        """
        self._ensure_loaded()

        # Split query into meaningful terms
        terms = re.split(r'[,;.\n()]+', query)
        terms = [t.strip().lower() for t in terms if t.strip() and len(t.strip()) > 1]

        if not terms:
            return {'query': query, 'total': 0, 'groups': [], 'matched_domains': [], 'all_items': []}

        matched_domains_info = []
        domain_code_prefixes = set()  # code prefixes from matched domains
        domain_sectors = set()        # sectors from matched domains
        unmatched_keywords = set()    # raw keywords for unfound terms

        # Phase 1: Check each term against the domain taxonomy
        for term in terms:
            best_domain_key, best_score = self._find_best_domain(term)
            if best_domain_key:
                domain_info = DOMAIN_MAP[best_domain_key]
                # Deduplicate
                if not any(d['key'] == best_domain_key for d in matched_domains_info):
                    matched_domains_info.append({
                        'key': best_domain_key,
                        'label': domain_info.get('label', best_domain_key),
                    })
                if domain_info.get('sectors'):
                    domain_sectors.update(domain_info['sectors'])
                if domain_info.get('code_prefixes'):
                    for p in domain_info['code_prefixes']:
                        domain_code_prefixes.add(p)
            else:
                unmatched_keywords.add(term)

        # If nothing at all matched, return empty
        if not domain_code_prefixes and not unmatched_keywords:
            return {'query': query, 'total': 0, 'groups': [], 'matched_domains': [], 'all_items': []}

        # Phase 2: Collect results
        results: dict[str, dict] = {}

        # Strategy A: Domain code prefix matching (focused, high-precision)
        if domain_code_prefixes:
            # Sort prefixes by length descending to match most specific first
            sorted_prefixes = sorted(domain_code_prefixes, key=len, reverse=True)
            for entry in self._codes:
                code = entry.get('code', '')
                if code in results:
                    continue
                # Check if code matches any domain prefix
                for prefix in sorted_prefixes:
                    if code.startswith(prefix):
                        results[code] = self._format_result(entry, 'domain')
                        break

        # Strategy B: Unmatched keyword search in names (fallback)
        if unmatched_keywords:
            for entry in self._codes:
                code = entry.get('code', '')
                if code in results:
                    continue
                name = (entry.get('name', '') or '').lower()
                for kw in unmatched_keywords:
                    if kw in name:
                        results[code] = self._format_result(entry, 'keyword')
                        break

        # Phase 3: Group by sector
        grouped: dict[str, dict] = {}
        for item in results.values():
            sec = item['sector']['code']
            if sec not in grouped:
                grouped[sec] = {
                    'sector': item['sector'],
                    'items': [],
                }
            grouped[sec]['items'].append(item)

        sorted_groups = []
        for sec in sorted(grouped.keys()):
            grouped[sec]['items'].sort(key=lambda x: x['code'])
            sorted_groups.append(grouped[sec])

        all_items = list(results.values())
        all_items.sort(key=lambda x: x['code'])
        if limit > 0:
            all_items = all_items[:limit]

        return {
            'query': query,
            'total': len(results),
            'groups': sorted_groups,
            'matched_domains': matched_domains_info,
            'all_items': all_items,
        }

    @staticmethod
    def _term_matches(domain_term: str, query_term: str) -> bool:
        """Check if a domain term matches a query term.

        Exact match for short terms (≤4 chars) to prevent false positives
        like 'it' matching inside 'ugostiteljstvo' or 'bar' in 'barbell'.
        Uses substring matching for longer terms.
        """
        dt = domain_term.lower()
        qt = query_term.lower()
        if dt == qt:
            return True
        # If either term is short, require exact match
        if len(qt) <= 4 or len(dt) <= 4:
            return False
        # For longer terms, substring match is fine
        return dt in qt or qt in dt

    def _find_best_domain(self, term: str) -> tuple[Optional[str], int]:
        """Find the best matching domain for a term using scoring.

        Prefers exact matches over substring matches to resolve conflicts
        (e.g. 'usluge' should match Usluge domain, not građevinarstvo which
        happens to have 'građevinske usluge' as a term).

        Returns:
            (domain_key, score) or (None, 0) if no match
        """
        best_key: Optional[str] = None
        best_score = 0

        for domain_key, domain_info in DOMAIN_MAP.items():
            domain_terms = domain_info.get('terms', [domain_key])
            for domain_term in domain_terms:
                if not self._term_matches(domain_term, term):
                    continue
                # Score: exact match best, domain-in-query medium, query-in-domain weak
                if domain_term == term:
                    score = 100
                elif domain_term in term:
                    score = 50
                else:  # term in domain_term (weakest signal)
                    score = 20

                if score > best_score:
                    best_score = score
                    best_key = domain_key

        return best_key, best_score

    # ─── Single code lookups ──────────────────────────────────────────────────

    def get_by_code(self, code: str) -> Optional[dict]:
        """Get a single KD entry by its code string.

        Args:
            code: e.g. '56.30' or '01.11'

        Returns:
            Full entry dict or None
        """
        self._ensure_loaded()
        entry = self._code_index.get(code.strip())
        if entry:
            return dict(entry)
        return None

    def validate(self, code: str) -> bool:
        """Check if a KD code exists in the database."""
        self._ensure_loaded()
        return code.strip() in self._code_index

    # ─── Metadata ─────────────────────────────────────────────────────────────

    def get_sectors(self) -> list[dict]:
        """Get all sectors with their codes and counts."""
        self._ensure_loaded()
        return list(self._sectors)

    def get_count(self) -> int:
        """Total number of KD codes."""
        self._ensure_loaded()
        return len(self._codes)

    # ─── Display formatting ───────────────────────────────────────────────────

    def format_for_display(self, code: str) -> str:
        """Format a KD code for display: 'xx.xx — Full name'."""
        entry = self.get_by_code(code)
        if entry:
            return f"{entry['code']} — {entry['name']}"
        return code

    def format_with_sector(self, code: str) -> str:
        """Format: 'xx.xx — Name (Sektor X)'."""
        entry = self.get_by_code(code)
        if entry:
            sec = entry.get('sector', {})
            return f"{entry['code']} — {entry['name']} (Sektor {sec.get('code', '?')})"
        return code

    def resolve_description(self, code: str) -> str:
        """Get the full description for a KD code."""
        entry = self.get_by_code(code)
        if entry:
            return entry.get('description', '')
        return ''

    # ─── Internal helpers ────────────────────────────────────────────────────

    def _format_result(self, entry: dict, match_type: str) -> dict:
        return {
            'code': entry.get('code', ''),
            'name': entry.get('name', ''),
            'sector': entry.get('sector', {}),
            'description': (entry.get('description', '') or '')[:300],
            'match_type': match_type,
        }

    def _list_all(self, limit: int, sector: str | None = None) -> list[dict]:
        """Return all codes, optionally filtered by sector."""
        entries = self._codes
        if sector:
            entries = [e for e in entries if e.get('sector', {}).get('code') == sector]

        return [
            self._format_result(e, 'all')
            for e in entries[:limit]
        ]


# ─── Module-level singleton ──────────────────────────────────────────────────

_reader_instance: KDReader | None = None


def get_kd_reader() -> KDReader:
    """Get or create the singleton KDReader instance."""
    global _reader_instance
    if _reader_instance is None:
        _reader_instance = KDReader()
    return _reader_instance
