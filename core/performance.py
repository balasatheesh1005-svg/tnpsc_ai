"""
TNPSC Nova AI - Developer Performance Monitor V1
Phase 7.0 Performance Engineering - Sprint 1.5

Lightweight developer-only performance monitoring framework.
Measures application render times, AI engine executions, database queries,
cache efficiency, memory usage, and slow operations.

When DEV_MODE = False, all recording functions execute near-zero overhead no-ops.
"""

import time
import functools
import tracemalloc
from typing import Dict, List, Any, Optional, Callable

# Global Developer Mode Toggle
DEV_MODE: bool = True

# Slow operation threshold in seconds (default 500ms)
SLOW_OPERATION_THRESHOLD: float = 0.5


class PerformanceMonitor:
    """Central performance collector and timing manager."""

    def __init__(self):
        self.reset_metrics()

    def reset_metrics(self) -> None:
        """Reset all recorded metrics for a new render cycle."""
        self._timers: Dict[str, float] = {}
        self._durations: Dict[str, float] = {}
        self._queries: List[Dict[str, Any]] = []
        self._cache_hits: Dict[str, int] = {}
        self._cache_misses: Dict[str, int] = {}
        self._engine_durations: Dict[str, float] = {}
        self._render_durations: Dict[str, float] = {}
        self._slow_operations: List[Dict[str, Any]] = []
        self._session_stats: Dict[str, Any] = {}
        self._render_start_time: float = time.perf_counter()

    def start_timer(self, name: str) -> None:
        """Start high-precision timer for a named operation."""
        if not DEV_MODE:
            return
        self._timers[name] = time.perf_counter()

    def end_timer(self, name: str) -> float:
        """Stop timer and return elapsed duration in seconds."""
        if not DEV_MODE:
            return 0.0
        start = self._timers.pop(name, None)
        if start is None:
            return 0.0
        duration = time.perf_counter() - start
        self._durations[name] = duration
        if duration >= SLOW_OPERATION_THRESHOLD:
            self._slow_operations.append({
                "name": name,
                "duration": duration,
            })
        return duration

    def record_query(self, table_name: str = "unknown", duration: float = 0.0, success: bool = True) -> None:
        """Record database query metrics."""
        if not DEV_MODE:
            return
        self._queries.append({
            "table": table_name,
            "duration": duration,
            "success": success,
        })
        if duration >= SLOW_OPERATION_THRESHOLD:
            self._slow_operations.append({
                "name": f"DB Query ({table_name})",
                "duration": duration,
            })

    def record_cache_hit(self, function_name: str = "unknown") -> None:
        """Record a cache hit for a function."""
        if not DEV_MODE:
            return
        self._cache_hits[function_name] = self._cache_hits.get(function_name, 0) + 1

    def record_cache_miss(self, function_name: str = "unknown") -> None:
        """Record a cache miss for a function."""
        if not DEV_MODE:
            return
        self._cache_misses[function_name] = self._cache_misses.get(function_name, 0) + 1

    def record_engine(self, engine_name: str = "unknown", duration: float = 0.0) -> None:
        """Record execution duration of an AI Engine."""
        if not DEV_MODE:
            return
        self._engine_durations[engine_name] = duration

    def record_render(self, section_name: str = "unknown", duration: float = 0.0) -> None:
        """Record rendering duration of a UI section."""
        if not DEV_MODE:
            return
        self._render_durations[section_name] = duration

    def record_memory(self) -> Dict[str, float]:
        """Record current memory usage metrics via tracemalloc if active."""
        if not DEV_MODE:
            return {"current_mb": 0.0, "peak_mb": 0.0}
        try:
            if not tracemalloc.is_tracing():
                tracemalloc.start()
            current, peak = tracemalloc.get_traced_memory()
            return {
                "current_mb": round(current / (1024 * 1024), 3),
                "peak_mb": round(peak / (1024 * 1024), 3),
            }
        except Exception:
            return {"current_mb": 0.0, "peak_mb": 0.0}

    def record_session(self, key: str, value: Any) -> None:
        """Record custom session statistic."""
        if not DEV_MODE:
            return
        self._session_stats[key] = value

    def get_query_summary(self) -> Dict[str, Any]:
        """Aggregate query metrics grouped by table."""
        if not self._queries:
            return {"total_count": 0, "total_time": 0.0, "by_table": {}}
        total_time = sum(q["duration"] for q in self._queries)
        by_table: Dict[str, Dict[str, Any]] = {}
        for q in self._queries:
            tbl = q["table"]
            if tbl not in by_table:
                by_table[tbl] = {"count": 0, "total_time": 0.0}
            by_table[tbl]["count"] += 1
            by_table[tbl]["total_time"] += q["duration"]
        return {
            "total_count": len(self._queries),
            "total_time": round(total_time, 4),
            "by_table": by_table,
        }

    def get_cache_summary(self) -> Dict[str, Any]:
        """Aggregate cache hits, misses, and hit ratio."""
        total_hits = sum(self._cache_hits.values())
        total_misses = sum(self._cache_misses.values())
        total_accesses = total_hits + total_misses
        hit_ratio = round((total_hits / total_accesses) * 100, 1) if total_accesses > 0 else 100.0
        return {
            "hits": total_hits,
            "misses": total_misses,
            "hit_ratio": hit_ratio,
            "hit_details": self._cache_hits,
            "miss_details": self._cache_misses,
        }

    def export_summary(self) -> Dict[str, Any]:
        """Export all current metrics as a structured dictionary."""
        overall_render = time.perf_counter() - self._render_start_time
        return {
            "overall_render": round(overall_render, 4),
            "engine_durations": {k: round(v, 4) for k, v in self._engine_durations.items()},
            "render_durations": {k: round(v, 4) for k, v in self._render_durations.items()},
            "query_summary": self.get_query_summary(),
            "cache_summary": self.get_cache_summary(),
            "slow_operations": self._slow_operations,
            "session_stats": self._session_stats,
        }

    def print_summary(self) -> str:
        """Generate and print the formatted TNPSC Nova AI Performance Report."""
        if not DEV_MODE:
            return ""

        summary = self.export_summary()
        lines = []
        lines.append("==================================================")
        lines.append("TNPSC Nova AI Performance Report")
        lines.append("==================================================")

        # UI & Engine Timings
        all_timings = {}
        all_timings.update(summary["render_durations"])
        all_timings.update(summary["engine_durations"])

        if all_timings:
            for op_name, dur in all_timings.items():
                label = f"{op_name:<30}"
                dots = "." * max(1, 31 - len(op_name))
                lines.append(f"{op_name} {dots} {dur:.2f} sec")
        else:
            lines.append("No engine/render timings recorded")

        # Database Query Summary
        q_sum = summary["query_summary"]
        lines.append("--------------------------------------------------")
        lines.append(f"Database Queries ............... {q_sum['total_count']}")
        lines.append(f"Total Query Time ............... {q_sum['total_time']:.2f} sec")
        
        # Table detail breakdown if present
        for tbl, data in q_sum.get("by_table", {}).items():
            lines.append(f"  • {tbl:<26} {data['count']} q ({data['total_time']:.3f} s)")

        # Cache Summary
        c_sum = summary["cache_summary"]
        lines.append("--------------------------------------------------")
        lines.append(f"Cache Hits ..................... {c_sum['hits']}")
        lines.append(f"Cache Misses ................... {c_sum['misses']}")
        lines.append(f"Hit Ratio ...................... {c_sum['hit_ratio']:.0f}%")

        # Slow Operations Warning
        if summary["slow_operations"]:
            lines.append("--------------------------------------------------")
            lines.append("⚠ Slow Operations (> 0.5s):")
            for slow in summary["slow_operations"]:
                lines.append(f"  ⚠ {slow['name']} ({slow['duration']:.3f} sec)")

        lines.append("--------------------------------------------------")
        lines.append(f"Overall Page Render ............ {summary['overall_render']:.2f} sec")
        lines.append("==================================================")

        report_text = "\n".join(lines)
        print(report_text)
        return report_text


# Global Singleton Instance
perf_monitor = PerformanceMonitor()


# Reusable API Wrappers & Helper Functions
def start_timer(name: str) -> None:
    perf_monitor.start_timer(name)


def end_timer(name: str) -> float:
    return perf_monitor.end_timer(name)


def record_query(table_name: str = "unknown", duration: float = 0.0, success: bool = True) -> None:
    perf_monitor.record_query(table_name, duration, success)


def record_cache_hit(function_name: str = "unknown") -> None:
    perf_monitor.record_cache_hit(function_name)


def record_cache_miss(function_name: str = "unknown") -> None:
    perf_monitor.record_cache_miss(function_name)


def record_engine(engine_name: str = "unknown", duration: float = 0.0) -> None:
    perf_monitor.record_engine(engine_name, duration)


def record_render(section_name: str = "unknown", duration: float = 0.0) -> None:
    perf_monitor.record_render(section_name, duration)


def record_memory() -> Dict[str, float]:
    return perf_monitor.record_memory()


def print_summary() -> str:
    return perf_monitor.print_summary()


def reset_metrics() -> None:
    perf_monitor.reset_metrics()


def export_summary() -> Dict[str, Any]:
    return perf_monitor.export_summary()


def track_query(table_name: str = "unknown", duration: float = 0.0, success: bool = True) -> None:
    record_query(table_name, duration, success)


def track_cache(hit: bool = True, function_name: str = "unknown") -> None:
    if hit:
        record_cache_hit(function_name)
    else:
        record_cache_miss(function_name)


def track_memory() -> Dict[str, float]:
    return record_memory()


def track_session(key: str, value: Any) -> None:
    perf_monitor.record_session(key, value)


def measure_time(module_name: str):
    """Reusable decorator to automatically time function execution."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not DEV_MODE:
                return func(*args, **kwargs)
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                elapsed = time.perf_counter() - start_time
                perf_monitor.record_engine(module_name, elapsed)
        return wrapper
    return decorator
