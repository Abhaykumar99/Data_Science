import matplotlib.pyplot as plt

# Sample data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores = [40, 45, 50, 55, 60, 65, 75, 85, 90]

plt.scatter(study_hours,exam_scores)
plt.title("Study Hours Vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

colors=['red' if score<50 else 'green' for score in exam_scores]
sizes=[score *2 for score in exam_scores]
plt.scatter(study_hours,exam_scores,c=colors,s=sizes)
plt.grid(True)
plt.show()

plt.scatter(study_hours, exam_scores, c=exam_scores, cmap='viridis')
plt.colorbar(label='Score')
plt.title('Scatter Plot with Colormap')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
for i in range(len(study_hours)):
    plt.annotate(f'S{i+1}',(study_hours[i] + 0.1,exam_scores[i]))
plt.grid(True)
plt.show()


# Assume two groups: Class A and Class B
class_a_hours = [2, 4, 6, 8]
class_a_scores = [45, 55, 65, 85]
 
class_b_hours = [1, 3, 5, 7, 9]
class_b_scores = [40, 50, 60, 70, 90]

plt.scatter(class_a_hours,class_a_scores,label='A',color="red")
plt.scatter(class_b_hours,class_b_scores,label="B",color='blue')
plt.title("Scatter Plot: Class A vs Class B ")
plt.xlabel('Hours..')
plt.ylabel("Score..")
plt.grid(True)
plt.show()