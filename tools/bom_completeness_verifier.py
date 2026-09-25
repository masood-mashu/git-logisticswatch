"""
bom_completeness_verifier.py - Verifies that all required component parts in bill of materials are allocated in inventory
"""
import sys
import json


def verify_bom_completeness(required_parts: str, allocated_parts: str):
    req = set([p.strip().upper() for p in required_parts.split(",") if p.strip()])
    alloc = set([p.strip().upper() for p in allocated_parts.split(",") if p.strip()])
    missing = req - alloc
    is_complete = len(missing) == 0
    return {"complete": is_complete, "missing_parts": list(missing), "status": "READY_FOR_PRODUCTION" if is_complete else "SHORTAGE_BLOCKED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "bom-completeness-verifier"}))
