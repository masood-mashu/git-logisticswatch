"""
hts_code_validator.py - Validates that international trade components specify a valid 6-digit HTS tariff code
"""
import sys
import json


def validate_hts_code(hts_code: str):
    import re
    cleaned = re.sub(r"[.\s]", "", hts_code.strip())
    is_valid = bool(re.match(r"^\d{6}(\d{2}|\d{4})?$", cleaned))
    return {"valid_hts": is_valid, "formatted_code": cleaned, "status": "VALID" if is_valid else "INVALID_HTS_SYNTAX"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "hts-code-validator"}))
