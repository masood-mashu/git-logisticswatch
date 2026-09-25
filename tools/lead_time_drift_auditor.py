"""
lead_time_drift_auditor.py - Detects suppliers whose actual lead time exceeds contractual quotes by more than 20%
"""
import sys
import json


def audit_lead_time_drift(actual_days: int, quoted_days: int, max_drift_pct: float = 20.0):
    drift_pct = round(((actual_days - quoted_days) / quoted_days) * 100, 1) if quoted_days > 0 else 0.0
    is_acceptable = drift_pct <= max_drift_pct
    return {"quoted_days": quoted_days, "actual_days": actual_days, "drift_percent": drift_pct, "acceptable": is_acceptable, "status": "APPROVED" if is_acceptable else "SUPPLIER_DRIFT_WARNING"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "lead-time-drift-auditor"}))
