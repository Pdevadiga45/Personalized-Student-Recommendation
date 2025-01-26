# Personalized-Student-Recommendation
A Python-based solution to analyze quiz performance and provide students with personalized recommendations to improve their preparation.

## Historical Data Visualizations

### 1.  Recommendations and Insights
Performance trends and actionable insights.  
Based on the visualization, the user should focus on topics with the highest **`priority score`**.  

### Priority Score Calculation and Significance

**How Priority Score is Calculated**  
The priority score ranks quiz topics based on their importance and relevance to the user's learning. It is computed using three key factors:  

1. **Weightage Factor (W_w)**  
   - Importance of the topic in the syllabus, derived from syllabus weightage percentages (source: Vedantu.com).  
   - Ensures high-weightage topics are prioritized.  

2. **Weakness Factor (W_r)**  
   - Indicates how much the user struggles with a topic.  
   - Calculated inversely from quiz scores, so lower performance increases the weakness factor.  

3. **Recency Factor (W_c)**  
   - Measures how recently the user attempted quizzes for the topic.  
   - Recent attempts have higher scores, while older attempts decay over time to maintain relevance.  

**Formula:**  
Priority Score = (Weightage Factor * W_w) + (Weakness Factor * W_r) + (Recency Factor * W_c)


**Significance of Priority Score**  
- **Focus on Weak Areas:** Helps identify and address topics where the user struggles most.  
- **Syllabus Alignment:** Ensures preparation focuses on high-weightage topics for maximum effectiveness.  
- **Dynamic and Adaptive:** Adapts to the user's evolving performance and learning history, emphasizing recent activity for up-to-date insights.  

By following these recommendations based on priority scores, users can optimize their study plans for improved preparation and outcomes.


![Historical Data](https://github.com/user-attachments/assets/679ad5f3-5869-4c9b-b768-18cffb7113bb)

### 2. Average Accuracy Across All Topics
Visual representation of the user's average accuracy across all quiz topics, offering insights into areas of strength and improvement opportunities.  

![Average Accuracy](https://github.com/user-attachments/assets/bcac31e6-ae68-411d-b45e-d7d6331a7266)


### 3. Average Accuracy Across All Topics
Visual representation of the user's average accuracy across all quiz topics, offering insights into areas of strength and improvement opportunities.  

## Student Persona

**What is a Student Persona?**  
A "persona" is a descriptive label assigned to a user based on their performance across quizzes. It categorizes users into distinct groups, providing insights into their strengths and areas for improvement.  

**How Personas are Determined**  
Personas are calculated by analyzing **average speed** and **accuracy**, dividing performance into four quadrants:  

1. **The Prodigy**  
   - High speed and high accuracy.  
   - Represents exceptional performance with balanced efficiency and precision.  

2. **The Speedster**  
   - High speed but lower accuracy.  
   - Indicates efficiency in answering but highlights room for improving precision.  

3. **The Perfectionist**  
   - High accuracy but lower speed.  
   - Reflects meticulousness and careful problem-solving with potential for increased efficiency.  

4. **The Explorer**  
   - Lower speed and lower accuracy.  
   - Signifies a learning phase with opportunities for growth and skill-building.

**Persona assigned based on the user's Historical Data provided**


Output for StudentPersona.py:

- User ID: YcDFSO4ZukTJnnFMgRNVwZTE4j42, Persona: The Prodigy
- User ID: userid1, Persona: The Speedster
- User ID: userid2, Persona: The Prodigy
- User ID: userid3, Persona: The Perfectionist
- User ID: userid4, Persona: The Explorer

![image](https://github.com/user-attachments/assets/4773d3df-c50c-4fad-b1ae-2212cb819d36)




