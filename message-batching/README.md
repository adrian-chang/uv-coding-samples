# Question: Optimal Batch Messaging Scheduler

## Problem Statement:

Send personalized messages to users based on their preferences. To optimize server load, the system processes messages in batches. Each batch can handle up to k messages at a time. Your task is to implement a function that groups users into batches such that:

Each batch contains at most k users.
Users with similar message templates are grouped together as much as possible to improve caching efficiency.
The total number of batches is minimized.
You are given:

A list of user profiles, where each profile contains:
user_id: A unique identifier for the user.
message_template: A personalized message template for the user (e.g., "Hi {name}, check out our latest offers!").
An integer k, representing the maximum number of users per batch.
Your goal is to implement a function schedule_batches that:

Takes the list of user profiles and the integer k as input.
Returns a list of batches, where each batch is a list of user_ids.

Example: 
```
users = [
    {"user_id": 1, "message_template": "Hi {name}, check out our latest offers!"},
    {"user_id": 2, "message_template": "Hey {name}, we have something special for you!"},
    {"user_id": 3, "message_template": "Hi {name}, check out our latest offers!"},
    {"user_id": 4, "message_template": "Hi {name}, check out our latest offers!"},
    {"user_id": 5, "message_template": "Hey {name}, we have something special for you!"},
    {"user_id": 6, "message_template": "Welcome back, {name}!"}
]

[
    [1, 3, 4],  # All users share the same message template
    [2, 5],     # Both users share the same message template
    [6]         # Only one user with this message template
]
```