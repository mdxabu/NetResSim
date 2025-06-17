> [!NOTE]
> This project is for educational purposes only!

# Evaluating Internet Resilience Under Simulated Regional Disruption Using RIPE Atlas

This project examines the impact of simulated regional network disruptions on Internet performance using real-world measurement data. The goal is to understand how large-scale events can influence Internet connectivity and routing dynamics, and to evaluate the resilience of Internet infrastructure under stress.

# Network Resilience Event Analysis

This project analyzes the impact of various network disruption events on Internet infrastructure, including natural disasters, submarine cable cuts, and geopolitical conflicts.

## Features

- Fetches data from RIPE RIS/RIPEstat for AS reachability
- Analyzes baseline, event, and recovery phases
- Generates comprehensive visualizations for each event
- Saves individual analysis plots with detailed metrics

## Events Analyzed

1. Croatia Earthquake 2020
2. Puerto Rico Earthquake 2020  
3. Hengchun Submarine Cable Cut 2006
4. SEA-ME-WE Disruption 2008
5. Israel Iran Conflict 2025
6. Nepal Earthquake 2015

## Usage

```bash
pip install -r requirements.txt
python netres_analysis.py
```

## Output

- Individual analysis plots saved in `output/` directory
- Detailed console output with metrics for each event phase
- Impact percentages and recovery rates


