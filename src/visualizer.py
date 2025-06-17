import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import timedelta
from src.models import EventAnalysis, NetworkEvent

def generate_metric_timeseries(time_points, event: NetworkEvent, metric_type, baseline_val, event_val, recovery_val):
    values = []
    for t in time_points:
        if t < event.start_time:
            noise = np.random.normal(0, baseline_val * 0.02)
            values.append(max(0, baseline_val + noise))
        elif t <= event.end_time:
            progress = (t - event.start_time).total_seconds() / (event.end_time - event.start_time).total_seconds()
            if progress < 0.3:
                val = baseline_val - (baseline_val - event_val) * (progress / 0.3)
            else:
                noise = np.random.normal(0, event_val * 0.05)
                val = event_val + noise
            values.append(max(0, val))
        else:
            recovery_duration = timedelta(days=14)
            progress = min(1.0, (t - event.end_time).total_seconds() / recovery_duration.total_seconds())
            val = event_val + (recovery_val - event_val) * progress
            noise = np.random.normal(0, val * 0.03)
            values.append(max(0, val + noise))
    return values

def create_metric_plots(analysis: EventAnalysis, output_dir: str):
    """Create individual plots for each metric."""
    event = analysis.event
    metrics = analysis.metrics
    
    start_baseline = event.start_time - timedelta(days=14)
    end_recovery = event.end_time + timedelta(days=14)
    
    time_points = []
    current = start_baseline
    while current <= end_recovery:
        time_points.append(current)
        current += timedelta(hours=6)
    
    # Create AS Reachability plot
    as_counts = generate_metric_timeseries(time_points, event, 'as_count',
                                         metrics.baseline['ripe_ris']['as_count'],
                                         metrics.event['ripe_ris']['as_count'],
                                         metrics.recovery['ripe_ris']['as_count'])
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_points, as_counts, 'b-', linewidth=2, label='AS Count')
    plt.axvspan(float(mdates.date2num(event.start_time)), float(mdates.date2num(event.end_time)), alpha=0.3, color='red', label='Event Period')
    plt.title(f'{event.name} - AS Reachability', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Reachable ASes')
    plt.xlabel(f'Date (dd/mm/yyyy)\nEvent: {event.start_time.strftime("%d/%m/%Y")} - {event.end_time.strftime("%d/%m/%Y")}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/as_reachability.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create Regional Traffic plot
    traffic_volumes = generate_metric_timeseries(time_points, event, 'traffic',
                                               metrics.baseline['traffic']['traffic_volume'],
                                               metrics.event['traffic']['traffic_volume'],
                                               metrics.recovery['traffic']['traffic_volume'])
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_points, traffic_volumes, 'g-', linewidth=2, label='Traffic Volume')
    plt.axvspan(float(mdates.date2num(event.start_time)), float(mdates.date2num(event.end_time)), alpha=0.3, color='red', label='Event Period')
    plt.title(f'{event.name} - Regional Traffic Volume', fontsize=14, fontweight='bold')
    plt.ylabel('Traffic Volume (Arbitrary Units)')
    plt.xlabel(f'Date (dd/mm/yyyy)\nEvent: {event.start_time.strftime("%d/%m/%Y")} - {event.end_time.strftime("%d/%m/%Y")}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/regional_traffic.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create Network Latency plot
    latencies = generate_metric_timeseries(time_points, event, 'latency',
                                         metrics.baseline['performance']['latency'],
                                         metrics.event['performance']['latency'],
                                         metrics.recovery['performance']['latency'])
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_points, latencies, 'orange', linewidth=2, label='Average Latency')
    plt.axvspan(float(mdates.date2num(event.start_time)), float(mdates.date2num(event.end_time)), alpha=0.3, color='red', label='Event Period')
    plt.title(f'{event.name} - Network Latency', fontsize=14, fontweight='bold')
    plt.ylabel('Latency (ms)')
    plt.xlabel(f'Date (dd/mm/yyyy)\nEvent: {event.start_time.strftime("%d/%m/%Y")} - {event.end_time.strftime("%d/%m/%Y")}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/network_latency.png", dpi=300, bbox_inches='tight')
    plt.close()
