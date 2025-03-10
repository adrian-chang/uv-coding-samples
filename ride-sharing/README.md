# Ride Sharing

## Problem Statement

Design a real-time analytics dashboard for a ride-sharing app. The system must:
* Track the moving average of ride fares over a sliding window of the last N rides.
* Support querying the top K busiest pickup locations (by ride count) in the last M minutes.
* Handle high throughput (e.g., thousands of ride events per second).

## Requirements

* Implement the core data structures/algorithms for these features.
* Optimize for both time and space complexity.
* Discuss trade-offs (e.g., exact vs. approximate solutions).