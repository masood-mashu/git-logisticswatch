"""
reorder_point_calculator.py - Calculates safety stock and economic reorder point where ROP is Daily Usage times Lead Time plus Safety Stock
"""
import sys
import json


def calculate_reorder_point(daily_usage: int, lead_time_days: int, safety_stock: int):
    rop = (daily_usage * lead_time_days) + safety_stock
    return {"daily_usage": daily_usage, "lead_time_days": lead_time_days, "safety_stock": safety_stock, "reorder_point": rop, "status": "CALCULATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "reorder-point-calculator"}))
