"""
KD 2025 Reader — search and validate KD codes from the official MONSTAT database.

Loads the JSON file generated from the KD 2025 PDF source and provides:
- Fast search by code or name
- Sector filtering
- Code validation and full description resolution
"""
import json
import os
from pathlib import Path
from typing import Optional

# Default path to the KD 2025 JSON
DEFAULT_KD_PATH = os.path.join(
    os.path.expanduser('~'), 'agera-knowledge', 'processed', 'kd-2025-djelatnosti.json'
)


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
                sectors_seen[sec_code] = sec
                sectors_seen[sec_code]['count'] = 0
            if sec_code:
                sectors_seen[sec_code]['count'] = sectors_seen[sec_code].get('count', 0) + 1

        self._sectors = sorted(sectors_seen.values(), key=lambda s: s['code'])

        # Sort codes naturally by code string
        self._codes.sort(key=lambda x: x.get('code', ''))
        self._loaded = True

    # ─── Public API ──────────────────────────────────────────────────────────

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
                    results.append({
                        'code': code,
                        'name': entry.get('name', ''),
                        'sector': entry.get('sector', {}),
                        'description': entry.get('description', '')[:200],
                        'match_type': 'code_prefix',
                    })

        # 2. Code contains match
        for entry in self._codes:
            code = entry.get('code', '')
            if sector and entry.get('sector', {}).get('code') != sector:
                continue
            if query_lower in code and code not in seen_codes:
                seen_codes.add(code)
                results.append({
                    'code': code,
                    'name': entry.get('name', ''),
                    'sector': entry.get('sector', {}),
                    'description': entry.get('description', '')[:200],
                    'match_type': 'code_contains',
                })

        # 3. Name contains match (lower priority)
        for entry in self._codes:
            code = entry.get('code', '')
            if sector and entry.get('sector', {}).get('code') != sector:
                continue
            if query_lower in entry.get('name', '').lower() and code not in seen_codes:
                seen_codes.add(code)
                results.append({
                    'code': code,
                    'name': entry.get('name', ''),
                    'sector': entry.get('sector', {}),
                    'description': entry.get('description', '')[:200],
                    'match_type': 'name_contains',
                })

        return results[:limit]

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

    def get_sectors(self) -> list[dict]:
        """Get all sectors with their codes and counts."""
        self._ensure_loaded()
        return list(self._sectors)

    def get_count(self) -> int:
        """Total number of KD codes."""
        self._ensure_loaded()
        return len(self._codes)

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

    # ─── Internal ────────────────────────────────────────────────────────────

    def _list_all(self, limit: int, sector: str | None = None) -> list[dict]:
        """Return all codes, optionally filtered by sector."""
        entries = self._codes
        if sector:
            entries = [e for e in entries if e.get('sector', {}).get('code') == sector]

        return [
            {
                'code': e['code'],
                'name': e['name'],
                'sector': e['sector'],
                'description': e.get('description', '')[:200],
                'match_type': 'all',
            }
            for e in entries[:limit]
        ]

    def resolve_description(self, code: str) -> str:
        """Get the full description for a KD code."""
        entry = self.get_by_code(code)
        if entry:
            return entry.get('description', '')
        return ''


# ─── Module-level singleton ──────────────────────────────────────────────────

_reader_instance: KDReader | None = None


def get_kd_reader() -> KDReader:
    """Get or create the singleton KDReader instance."""
    global _reader_instance
    if _reader_instance is None:
        _reader_instance = KDReader()
    return _reader_instance
