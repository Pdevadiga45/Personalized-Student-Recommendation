import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import json
from collections import defaultdict
# Load data from a JSON file
with open(r'D:\internassignment\HistoricalData.json', 'r') as file:
    data = json.load(file)


# Calculate average speed and accuracy for each quiz
speeds = [int(entry["speed"]) for entry in data]
accuracies = [int(entry["accuracy"].replace('%', '')) for entry in data]

# Calculate overall average speed and accuracy
avg_speed = np.mean(speeds)
avg_accuracy = np.mean(accuracies)

# Determine persona based on overall averages
if avg_speed > 50 and avg_accuracy > 50:
    persona = "The Prodigy"
elif avg_speed > 50 and avg_accuracy <= 50:
    persona = "The Speedster"
elif avg_speed <= 50 and avg_accuracy > 50:
    persona = "The Perfectionist"
else:
    persona = "The Explorer"

# Print the assigned persona
print(f"User ID: {data[0]['user_id']}, Persona: {persona}")

# Optional: Visualize the data distribution
plt.scatter(speeds, accuracies, color='blue')
plt.axvline(50, color='red', linestyle='--', label='Median Speed')
plt.axhline(50, color='green', linestyle='--', label='Median Accuracy')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Speed')
plt.ylabel('Accuracy')
plt.title('User Performance Distribution')
plt.legend()
plt.show()