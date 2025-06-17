import datetime
from src.models import NetworkEvent, EventAnalysis
from src.analyzer import gather_metrics_for_event, analyze_individual_event

def main():
    events = [
        NetworkEvent(
            name="Croatia Earthquake 2020",
            event_type="natural_disaster",
            location="Croatia",
            start_time=datetime.datetime(2020, 3, 22, 5, 24),
            end_time=datetime.datetime(2020, 3, 23, 0, 0),
            description="Magnitude 5.3 earthquake in Zagreb, Croatia"
        ),
        NetworkEvent(
            name="Puerto Rico Earthquake 2020",
            event_type="natural_disaster",
            location="Puerto Rico",
            start_time=datetime.datetime(2020, 1, 7, 8, 24),
            end_time=datetime.datetime(2020, 1, 8, 0, 0),
            description="Magnitude 6.4 earthquake in Puerto Rico"
        ),
        NetworkEvent(
            name="Hengchun Submarine Cable Cut 2006",
            event_type="cable_cut",
            location="Taiwan",
            start_time=datetime.datetime(2006, 12, 26, 12, 26),
            end_time=datetime.datetime(2006, 12, 30, 0, 0),
            description="Earthquake-induced submarine cable cut near Hengchun, Taiwan"
        ),
        NetworkEvent(
            name="SEA-ME-WE Disruption 2008",
            event_type="cable_cut",
            location="Mediterranean Sea",
            start_time=datetime.datetime(2008, 1, 30, 8, 0),
            end_time=datetime.datetime(2008, 2, 2, 0, 0),
            description="Multiple submarine cable cuts affecting SEA-ME-WE-4 and FLAG"
        ),
        NetworkEvent(
            name="Israel Iran Conflict 2025",
            event_type="infrastructure_disruption",
            location="Middle East",
            start_time=datetime.datetime(2025, 5, 1, 0, 0),
            end_time=datetime.datetime(2025, 5, 10, 0, 0),
            description="Major regional conflict affecting Internet infrastructure"
        ),
        NetworkEvent(
            name="Nepal Earthquake 2015",
            event_type="natural_disaster",
            location="Nepal",
            start_time=datetime.datetime(2015, 4, 25, 11, 56),
            end_time=datetime.datetime(2015, 4, 26, 0, 0),
            description="Magnitude 7.8 earthquake in Nepal"
        ),
    ]

    event_analyses = []
    for event in events:
        print(f"Gathering metrics for {event.name}...")
        metrics = gather_metrics_for_event(event)
        event_analyses.append(EventAnalysis(event=event, metrics=metrics))

    for analysis in event_analyses:
        analyze_individual_event(analysis)
    
    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"Analyzed {len(event_analyses)} events")
    print("Individual analysis plots saved in 'output/<event_name>/' directories")

if __name__ == "__main__":
    main()
