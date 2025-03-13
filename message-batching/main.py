from collections import defaultdict

def message_batches(users, k):
    result = []
    message_map = defaultdict(list)
    for user in users:
        user_id = user["user_id"]
        message_template = user["message_template"]
        target = message_map[message_template]
        if len(target) == k:
            result.append(target)
            message_map[message_template] = []
        message_map[message_template].append(user_id)
    for _, list_item in message_map.items():
        result.append(list_item)
    return result

if __name__ == "__main__":
    users_1 = [
        {"user_id": 1, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 2, "message_template": "Hey {name}, we have something special for you!"},
        {"user_id": 3, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 4, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 5, "message_template": "Hey {name}, we have something special for you!"},
        {"user_id": 6, "message_template": "Welcome back, {name}!"}
    ]
    output_1 = message_batches(users_1, 3)
    print(output_1)

    users_2 = [
        {"user_id": 1, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 2, "message_template": "Hey {name}, we have something special for you!"},
        {"user_id": 3, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 4, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 5, "message_template": "Hi {name}, check out our latest offers!"},
        {"user_id": 5, "message_template": "Hey {name}, we have something special for you!"},
        {"user_id": 6, "message_template": "Welcome back, {name}!"}
    ]
    output_2 = message_batches(users_2, 3)
    print(output_2)