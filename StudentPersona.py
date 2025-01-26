import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import json
from collections import defaultdict

with open(r'D:\internassignment\HistoricalData.json', 'r') as file:
    data = json.load(file)
user_data = []

# Loop through the data to aggregate speed and accuracy for each user
for entry in data:
    user_id = entry["user_id"]
    speed = int(entry["speed"])
    accuracy = int(entry["accuracy"].replace('%', ''))
    correct_answers = int(entry["correct_answers"])
    total_answered = correct_answers + int(entry["incorrect_answers"])

    user_found = next((user for user in user_data if user["user_id"] == user_id), None)
    
    if user_found:
        user_found["total_speed"] += speed
        user_found["total_accuracy"] += (correct_answers / total_answered) * 100  
        user_found["count"] += 1
    else:
        # Add new user to the list
        user_data.append({
            "user_id": user_id,
            "total_speed": speed,
            "total_accuracy": (correct_answers / total_answered) * 100, 
            "count": 1
        })

# Calculate average speed and accuracy for each user
user_averages = []
for user in user_data:
    avg_speed = user["total_speed"] / user["count"]
    avg_accuracy = user["total_accuracy"] / user["count"]
    user_averages.append({
        "user_id": user["user_id"],
        "avg_speed": avg_speed,
        "avg_accuracy": avg_accuracy
    })


fake_data = [
    {"user_id": "userid1", "avg_speed": "90", "avg_accuracy": "20%"},
    {"user_id": "userid2", "avg_speed": "85", "avg_accuracy": "80%"},
    {"user_id": "userid3", "avg_speed": "30", "avg_accuracy": "95%"},
    {"user_id": "userid4", "avg_speed": "35", "avg_accuracy": "30%"},
]

    # Appending sample_data from more users for better visualization

for entry in fake_data:
    user_id = entry["user_id"]
    avg_speed = int(entry["avg_speed"])     
    avg_accuracy = int(entry["avg_accuracy"].replace('%', ''))  

    user_averages.append({
        "user_id": user_id,
        "avg_speed": avg_speed,
        "avg_accuracy": avg_accuracy
    })

for averages in user_averages:
    avg_speed = averages["avg_speed"]
    avg_accuracy = averages["avg_accuracy"]
    
    if avg_speed > 50 and avg_accuracy > 50:
        persona = "The Prodigy"
    elif avg_speed > 50 and avg_accuracy <= 50:
        persona = "The Speedster"
    elif avg_speed <= 50 and avg_accuracy > 50:
        persona = "The Perfectionist"
    else:
        persona = "The Explorer"
    
    print(f"User ID: {averages['user_id']}, Persona: {persona}")

# Plot each user's average speed and accuracy
for averages in user_averages:
    plt.scatter(averages['avg_speed'], averages['avg_accuracy'], label=averages['user_id'])

plt.axvline(50, color='red', linestyle='--', label='Speed = 50')
plt.axhline(50, color='green', linestyle='--', label='Accuracy = 50')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Average Speed')
plt.ylabel('Average Accuracy')
plt.title('Users Performance Distribution')
plt.text(75, 75, "The Prodigy", fontsize=12, ha='center', va='center')
plt.text(75, 25, "The Speedster", fontsize=12, ha='center', va='center')
plt.text(25, 75, "The Perfectionist", fontsize=12, ha='center', va='center')
plt.text(25, 25, "The Explorer", fontsize=12, ha='center', va='center')
plt.legend()
plt.grid()
plt.show()
