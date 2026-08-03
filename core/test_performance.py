"""
Unit tests for Developer Performance Monitor V1 (core/performance.py).
Tests timer execution, query logging, cache tracking, slow operation detection,
report generation, and DEV_MODE toggle behavior.
"""

import time
import unittest
from core.performance import (
    PerformanceMonitor,
    start_timer,
    end_timer,
    record_query,
    record_cache_hit,
    record_cache_miss,
    record_engine,
    record_render,
    record_memory,
    print_summary,
    reset_metrics,
    export_summary,
    measure_time,
    track_query,
    track_cache,
    perf_monitor,
)
import core.performance as perf_module


class TestPerformanceMonitor(unittest.TestCase):

    def setUp(self):
        perf_module.DEV_MODE = True
        reset_metrics()

    def tearDown(self):
        perf_module.DEV_MODE = True
        reset_metrics()

    def test_timer_execution(self):
        start_timer("test_op")
        time.sleep(0.02)
        dur = end_timer("test_op")
        self.assertGreaterEqual(dur, 0.015)
        summary = export_summary()
        self.assertIn("test_op", perf_monitor._durations)

    def test_measure_time_decorator(self):
        @measure_time("Test Engine")
        def dummy_engine():
            time.sleep(0.01)
            return "ok"

        res = dummy_engine()
        self.assertEqual(res, "ok")
        summary = export_summary()
        self.assertIn("Test Engine", summary["engine_durations"])
        self.assertGreaterEqual(summary["engine_durations"]["Test Engine"], 0.008)

    def test_query_recording(self):
        record_query("profiles", 0.031, success=True)
        record_query("mentor_memory", 0.019, success=True)
        record_query("profiles", 0.025, success=True)

        summary = export_summary()
        q_sum = summary["query_summary"]
        self.assertEqual(q_sum["total_count"], 3)
        self.assertAlmostEqual(q_sum["total_time"], 0.075, places=3)
        self.assertEqual(q_sum["by_table"]["profiles"]["count"], 2)
        self.assertEqual(q_sum["by_table"]["mentor_memory"]["count"], 1)

    def test_cache_monitoring(self):
        for _ in range(18):
            record_cache_hit("load_all_pyq")
        for _ in range(2):
            record_cache_miss("load_all_pyq")

        c_sum = perf_monitor.get_cache_summary()
        self.assertEqual(c_sum["hits"], 18)
        self.assertEqual(c_sum["misses"], 2)
        self.assertEqual(c_sum["hit_ratio"], 90.0)

    def test_slow_operation_detection(self):
        # Trigger slow operation (> 0.5s)
        perf_monitor._timers["slow_op"] = time.perf_counter() - 0.6
        perf_monitor.end_timer("slow_op")

        summary = export_summary()
        self.assertTrue(any(slow["name"] == "slow_op" for slow in summary["slow_operations"]))

    def test_print_summary_formatting(self):
        record_render("Dashboard Render", 0.72)
        record_engine("Learning Engine", 0.18)
        record_engine("Study Planner", 0.11)
        record_query("profiles", 0.031, success=True)
        record_cache_hit("test_func")

        report = print_summary()
        self.assertIn("TNPSC Nova AI Performance Report", report)
        self.assertIn("Dashboard Render", report)
        self.assertIn("Learning Engine", report)
        self.assertIn("Database Queries", report)
        self.assertIn("Cache Hits", report)

    def test_dev_mode_false_no_overhead(self):
        perf_module.DEV_MODE = False
        reset_metrics()

        start_timer("disabled_timer")
        dur = end_timer("disabled_timer")
        record_query("disabled_table", 0.5, success=True)
        record_cache_hit("disabled_cache")

        summary = export_summary()
        self.assertEqual(dur, 0.0)
        self.assertEqual(summary["query_summary"]["total_count"], 0)
        self.assertEqual(summary["cache_summary"]["hits"], 0)
        self.assertEqual(print_summary(), "")


if __name__ == "__main__":
    unittest.main()
