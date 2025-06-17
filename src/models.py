from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import datetime

@dataclass
class NetworkEvent:
    name: str
    event_type: str
    location: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    description: Optional[str] = None

@dataclass
class MetricWindow:
    baseline: Dict[str, Any] = field(default_factory=dict)
    event: Dict[str, Any] = field(default_factory=dict)
    recovery: Dict[str, Any] = field(default_factory=dict)

@dataclass
class EventAnalysis:
    event: NetworkEvent
    metrics: MetricWindow
