import json
import matplotlib.pyplot as plt

with open(r'D:\internassignment\CurrentQuizUserDetails.json', 'r') as file:
    data = json.load(file)


# Convert values to integers (if they are not already)
data['correct_answers'] = int(data['correct_answers'])
data['incorrect_answers'] = int(data['incorrect_answers'])
data['total_questions'] = int(data['total_questions'])

# Calculate unattempted questions
unattempted_questions = data['total_questions'] - (data['correct_answers'] + data['incorrect_answers'])

# Prepare data for the stacked bar plot
labels = ['Correct Answers', 'Incorrect Answers', 'Unattempted Questions']
values = [data['correct_answers'], data['incorrect_answers'], unattempted_questions]

# Create the bar plot
plt.figure(figsize=(8, 6))

# Set the x locations for the bars
x = range(len(labels))

# Create bars
plt.bar(x, values, color=['green', 'red', 'gray'])

# Add labels and title
plt.xticks(x, labels)  # Set the x-ticks to the labels
plt.xlabel('Question Type')
plt.ylabel('Number of Questions')
plt.title('Quiz Results Breakdown')
plt.tight_layout()

# Show the plot
plt.show()

# Calculate attempted questions
attempted_questions = data['correct_answers'] + data['incorrect_answers']

total_questions=int(data['total_questions'])

# Check if the user has attempted 40% or more of the total questions
if attempted_questions >= 0.4 * total_questions:
    print(f"User ID: {data['user_id']}, Accuracy: {data['accuracy']}, Speed: {data['speed']}")
else:
    print("To provide a fair evaluation of the quiz, it's important to attempt a sufficient number of questions. Please aim to attempt more questions next time.")