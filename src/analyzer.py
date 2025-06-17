from src.models import NetworkEvent, MetricWindow, EventAnalysis
from src.data_fetchers import (
    fetch_ripe_ris_data, fetch_ripe_atlas_data, fetch_outage_detection_data,
    fetch_traffic_analytics, fetch_performance_metrics
)
from src.visualizer import create_metric_plots
import os

def gather_metrics_for_event(event: NetworkEvent) -> MetricWindow:
    metrics = MetricWindow()
    for window in ['baseline', 'event', 'recovery']:
        getattr(metrics, window)['ripe_ris'] = fetch_ripe_ris_data(event, window)
        getattr(metrics, window)['ripe_atlas'] = fetch_ripe_atlas_data(event, window)
        getattr(metrics, window)['outage'] = fetch_outage_detection_data(event, window)
        getattr(metrics, window)['traffic'] = fetch_traffic_analytics(event, window)
        getattr(metrics, window)['performance'] = fetch_performance_metrics(event, window)
    return metrics

def analyze_individual_event(analysis: EventAnalysis):
    event = analysis.event
    metrics = analysis.metrics

    event_dir = f"output/{event.name.replace(' ', '_').replace('/', '_')}"
    os.makedirs(event_dir, exist_ok=True)

    create_metric_plots(analysis, event_dir)

    print(f"\n{'='*60}")
    print(f"DETAILED ANALYSIS: {event.name}")
    print(f"{'='*60}")
    print(f"Event Type: {event.event_type}")
    print(f"Location: {event.location}")
    print(f"Duration: {event.start_time.strftime('%d/%m/%Y %H:%M')} to {event.end_time.strftime('%d/%m/%Y %H:%M')}")
    print(f"Description: {event.description}")
    print(f"\nMETRICS ANALYSIS:")
    print(f"{'Phase':12} | {'AS Count':>8} | {'Traffic':>8} | {'Latency':>8} | {'Outages':>8}")
    print("-" * 60)

    for phase in ['baseline', 'event', 'recovery']:
        phase_metrics = getattr(metrics, phase)
        print(f"{phase.capitalize():12} | "
              f"{phase_metrics['ripe_ris']['as_count']:8} | "
              f"{phase_metrics['traffic']['traffic_volume']:8} | "
              f"{phase_metrics['performance']['latency']:8} | "
              f"{phase_metrics['outage']['unreachable_blocks']:8}")

    baseline_as = metrics.baseline['ripe_ris']['as_count']
    event_as = metrics.event['ripe_ris']['as_count']
    recovery_as = metrics.recovery['ripe_ris']['as_count']

    as_impact = ((baseline_as - event_as) / baseline_as) * 100 if baseline_as > 0 else 0
    recovery_rate = ((recovery_as - event_as) / (baseline_as - event_as)) * 100 if (baseline_as - event_as) > 0 else 0

    print(f"\nIMPACT SUMMARY:")
    print(f"AS Reachability Impact: {as_impact:.1f}% reduction during event")
    print(f"Recovery Rate: {recovery_rate:.1f}% recovered in recovery phase")
    print(f"Analysis saved to: {event_dir}/")
