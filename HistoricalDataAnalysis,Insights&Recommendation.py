import json
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
with open(r'D:\internassignment\HistoricalData.json', 'r') as file:
    data = json.load(file)

# Sort the data list from latest to oldest based on 'started_at' i.e Latest to Oldest
data = sorted(data, key=lambda x: x['started_at'], reverse=True)

#Source for weightage: Vedantu.com (PS I have added the quiz topics to their respective chapters in a list, mapping them according to their appropriate weightage)
weightageList = [
    {"Subject": "Botany", "Chapter": ["Genetics and Evolution","PRINCIPLES OF INHERITANCE AND VARIATION"], "Weightage (%)": 24},
    {"Subject": "Botany", "Chapter": ["Ecology and Environment"], "Weightage (%)": 16},
    {"Subject": "Botany", "Chapter": ["Plant Physiology"], "Weightage (%)": 13},
    {"Subject": "Botany", "Chapter": ["Plant Diversity"], "Weightage (%)": 12},
    {"Subject": "Botany", "Chapter": ["Cell Structure & Function"], "Weightage (%)": 10},
    {"Subject": "Botany", "Chapter": ["Plant Reproduction"], "Weightage (%)": 9},
    {"Subject": "Botany", "Chapter": ["Morphology of Flowering Plants"], "Weightage (%)": 7},
    {"Subject": "Botany", "Chapter": ["Plant Anatomy"], "Weightage (%)": 4},
    {"Subject": "Botany", "Chapter": ["Bio-molecule"], "Weightage (%)": 3},
    {"Subject": "Zoology", "Chapter": ["Human Physiology","Body Fluids and Circulation","Respiration and Gas Exchange"], "Weightage (%)": 45},
    {"Subject": "Zoology", "Chapter": ["Human Reproduction & Reproductive Health","Human Reproduction","Reproductive Health"], "Weightage (%)": 18},
    {"Subject": "Zoology", "Chapter": ["Animal Kingdom"], "Weightage (%)": 10},
    {"Subject": "Zoology", "Chapter": ["Origin & Evolution"], "Weightage (%)": 10},
    {"Subject": "Zoology", "Chapter": ["Human Health & Diseases","human health and disease"], "Weightage (%)": 9},
    {"Subject": "Zoology", "Chapter": ["Structural Organization in Animals"], "Weightage (%)": 5},
    {"Subject": "Zoology", "Chapter": ["Animal Husbandry"], "Weightage (%)": 3},
    {"Subject": "Zoology", "Chapter": ["Biology and Human Welfare","microbes in human welfare"], "Weightage (%)": 2}
]
#Factors used to calculate the priority score for every quiz topic 
W_w = 0.6  # Weightage constant
W_r = 0.3  # Weakness constant
W_c = 0.1  # Recency constant

# (lower score = higher weakness)
max_score = max(entry["score"] for entry in data)
min_score = min(entry["score"] for entry in data)
score_range = max_score - min_score if max_score != min_score else 1 

for entry in data:
    score = entry["score"]
    entry["weakness_factor"] = 1 - (score - min_score) / score_range  

#(most recent date = highest factor)
current_date = datetime.now()
timestamps = [datetime.fromisoformat(entry["started_at"].replace("Z", "")) for entry in data]
most_recent = max(timestamps)
least_recent = min(timestamps)
time_range = (most_recent - least_recent).days if (most_recent - least_recent).days > 0 else 1

# Define a decay factor (e.g., 0.01 per day) and a floor value
decay_per_day = 0.01
floor_value = 0.1  # Minimum recency factor

for entry, timestamp in zip(data, timestamps):
    days_since = (most_recent - timestamp).days
    # Calculate the decay based on the number of days since the most recent quiz
    decay = days_since * decay_per_day
    # Ensure the recency factor is not below the floor value
    entry["recency_factor"] = max(floor_value, 1 - decay)  # Normalize: most recent = 1, oldest >= floor_value

max_weightage = 100
min_weightage = 0
weightage_range = max_weightage - min_weightage if max_weightage != min_weightage else 1

# Create a dictionary from weightageList for quick lookup
weightage_dict = {}
for entry in weightageList:
    for chapter_name in entry["Chapter"]:
        weightage_dict[chapter_name.lower()] = entry["Weightage (%)"]

# Step 4: Aggregate data by topic
topic_data = defaultdict(list)

for entry in data:
    topic = entry["quiz"]["topic"].lower().strip()
    weightage = weightage_dict.get(topic, 0)  
    entry["weightage_factor"] = (weightage - min_weightage) / weightage_range
    topic_data[topic].append(entry)


# Calculate average accuracy across each unique topic
topic_accuracy = {}
topic_count = {}

for entry in data:
    topic = entry['quiz']['topic'].strip().lower()  #to make sure score across same topics are grouped together
    accuracy_str = entry['accuracy']
    accuracy_value = int(accuracy_str.replace('%', '').strip())  
    
    if topic not in topic_accuracy:
        topic_accuracy[topic] = 0
        topic_count[topic] = 0
    
    topic_accuracy[topic] += accuracy_value  
    topic_count[topic] += 1  

#Calculate average factors and priority score for each topic
topic_priority_scores = []

for topic, entries in topic_data.items():
    avg_weightage = sum(entry["weightage_factor"] for entry in entries) / len(entries)
    avg_weakness = sum(entry["weakness_factor"] for entry in entries) / len(entries)
    avg_recency = sum(entry["recency_factor"] for entry in entries) / len(entries)

    priority_score = (
        avg_weightage * W_w +
        avg_weakness * W_r +
        avg_recency * W_c
    )
    
    # Calculate average accuracy for the topic
    average_topic_accuracy = topic_accuracy[topic] / topic_count[topic] if topic_count[topic] > 0 else 0
    
    # Append each topic, its priority score, and average accuracy as a dictionary
    topic_priority_scores.append({
        "topic": topic,
        "priority_score": priority_score,
        "average_accuracy": average_topic_accuracy
    })

# Output results
for entry in topic_priority_scores:
    topic = entry["topic"]
    priority_score = entry["priority_score"]
    average_accuracy = entry["average_accuracy"]
    print(f"Topic: {topic.capitalize()}, Priority Score: {priority_score:.2f}, Average Accuracy: {average_accuracy:.2f}%")

for entry in data:
    print(f"Quiz Topic: {entry['quiz']['topic']}, "
          f"Weightage Factor: {entry['weightage_factor']:.2f}, "
          f"Weakness Factor: {entry['weakness_factor']:.2f}, "
          f"Recency Factor: {entry['recency_factor']:.2f} ")
    
    
topics = [entry["topic"] for entry in topic_priority_scores]
scores = [entry["priority_score"] for entry in topic_priority_scores]
average_accuracies = [entry["average_accuracy"] for entry in topic_priority_scores]

# Plot Priority Scores
plt.figure(figsize=(10, 6))
plt.bar(topics, scores, color='skyblue')
plt.xlabel('Topics')
plt.ylabel('Priority Score')
plt.title('Priority Score by Topic')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Plot Average Accuracies
plt.figure(figsize=(10, 6))
plt.bar(topics, average_accuracies, color='lightgreen')
plt.xlabel('Topics')
plt.ylabel('Average Accuracy (%)')
plt.title('Average Accuracy by Topic')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()