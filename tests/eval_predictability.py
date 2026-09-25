"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitLogisticsWatch.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.reorder_point_calculator import *
from tools.bom_completeness_verifier import *
from tools.lead_time_drift_auditor import *
from tools.hts_code_validator import *

class TestGitLogisticsWatchPredictability(unittest.TestCase):

    def test_01_reorder_point_calculation(self):
        res = calculate_reorder_point(daily_usage=10, lead_time_days=14, safety_stock=50)
        self.assertEqual(res["reorder_point"], 190)

    def test_02_bom_shortage_detected(self):
        res = verify_bom_completeness("PART_A,PART_B,PART_C", "PART_A,PART_B")
        self.assertFalse(res["complete"])
        self.assertIn("PART_C", res["missing_parts"])

    def test_03_lead_time_drift_flagged(self):
        res = audit_lead_time_drift(actual_days=30, quoted_days=20, max_drift_pct=20.0)
        self.assertFalse(res["acceptable"])
        self.assertEqual(res["status"], "SUPPLIER_DRIFT_WARNING")


if __name__ == "__main__":
    unittest.main()
