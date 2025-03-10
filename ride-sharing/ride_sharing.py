from collections import defaultdict
import heapq

class RideAnalytics:

    def __init__(self, window_size: int, location_capacity: int):
        # Initialize for N-ride average and top-K locations
        self.window_size = window_size
        self.location_capacity = location_capacity
        self.rolling_sum = 0
        self.current_rides = []
        self.location_ride = defaultdict(list)

    def record_ride(self, fare: float, pickup_location: str, timestamp: int):
        # Process a ride event
        # assume ride events are coming inrelative order
        # if > self.current_rides > n, drop oldest one and add
        if len(self.current_rides) >= self.window_size:
            oldest_ride_fare = self.current_rides.pop()
            self.rolling_sum -= oldest_ride_fare
        self.rolling_sum += fare
        self.current_rides.insert(0, fare)
        location_ride = self.location_ride[pickup_location]
        if len(location_ride) >= self.location_capacity:
            location_ride.pop()
        location_ride.insert(0, timestamp)

    def get_moving_average(self) -> float:
        # Return average fare over the last N rides
        # o(1), take rolling sum divide by length of stored rides
        # assume if less than n rides, average is over all rides seen currently
        return self.rolling_sum / len(self.current_rides)

    def get_top_locations(self, minutes: int, k: int) -> list[str]:
        # Return top K locations with most rides in the last M minutes
        temp_heap = []
        #print(self.location_ride)
        for location, rides in self.location_ride.items():
            local_sum = 0
            for ride in rides:
                if ride >= minutes:
                    local_sum += 1
            if local_sum > 0:
                heapq.heappush(temp_heap, (local_sum, location))
        #print(temp_heap)
        return [x[1] for x in heapq.nlargest(k, temp_heap)]


if __name__ == "__main__":
    r = RideAnalytics(100, 10)
    r.record_ride(1.0, "SF", 1)
    r.record_ride(2.0, "SF", 2)
    r.record_ride(1.5, "LA", 3)
    print(r.get_moving_average())
    print(r.get_top_locations(3, 1))


    r = RideAnalytics(10, 1)
    r.record_ride(1.0, "SF", 1)
    r.record_ride(2.0, "SF", 2)
    r.record_ride(1.5, "LA", 3)
    print(r.get_moving_average())
    print(r.get_top_locations(3, 1))

    r = RideAnalytics(10, 2)
    r.record_ride(1.0, "SFO", 1)
    r.record_ride(2.0, "LAX", 2)
    r.record_ride(1.5, "PDX", 3)
    r.record_ride(1.5, "PDX", 4)
    print(r.get_moving_average())
    print(r.get_top_locations(4, 2))
