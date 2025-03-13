import heapq

def maximize_traffic_greedy(messages, budget):
    heap = []
    for message in messages:
        heapq.heappush(heap, (-(message["traffic"] / message["cost"]), message))
    output = {
        "max_traffic": 0,
        "selected_users": []
    }
    while len(heap) > 0:
        (_, message) = heapq.heappop(heap)
        if budget - message["cost"] >= 0:
            output["max_traffic"] += message["traffic"]
            output["selected_users"].append(message["user_id"])
        budget -= message["cost"]
        if budget == 0:
            return output
    return output


if __name__ == "__main__":
    messages = [
        {"user_id": 1, "cost": 10, "traffic": 60},
        {"user_id": 2, "cost": 20, "traffic": 100},
        {"user_id": 3, "cost": 30, "traffic": 120},
        {"user_id": 4, "cost": 15, "traffic": 80},
        {"user_id": 5, "cost": 25, "traffic": 90}
    ]
    budget = 50
    print(maximize_traffic_greedy(messages, budget))