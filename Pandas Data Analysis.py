import pandas as pd
import numpy as np

# Create sample dataset
np.random.seed(42)
n_students = 200

data = {
    'student_id': range(1000, 1000 + n_students),
    'major': np.random.choice(['CS', 'Math', 'Physics', 'Biology'], n_students),
    'year': np.random.choice([1, 2, 3, 4], n_students),
    'exam_score': np.random.normal(75, 10, n_students).clip(0, 100),
    'assignments_completed': np.random.randint(0, 11, n_students),
    'hours_studied': np.random.normal(15, 5, n_students).clip(1, 40)
}

df = pd.DataFrame(data)

# Introduce some NaN values
df.loc[np.random.choice(n_students, 10), 'exam_score'] = np.nan
df.loc[np.random.choice(n_students, 5), 'hours_studied'] = np.nan

#TASK 1; Data Cleaning and Exploration

# TODO: Display basic information about the dataset, Identify and count missing values
print(df.info())
print("\nMissing vlaues per column:")

# TODO: Fill missing exam_score with the mean score for the student's major
df['exam_score'] = df['exam_score'].fillna(
    df.groupby('major')['exam_score'].transform('mean')
)
# TODO: Fill missing hours_studied with the median for the student's year
df['hours_studied'] = df['hours_studied'].fillna(
    df.groupby('year')['hours_studied'].transform('median')
)

# Task 2: Analysis (10 points)
# TODO: Calculate and display the average exam_score by major
print(df.groupby("major")["exam_score"].mean())

# TODO: Find the major with the highest average exam_score
best_major = df.groupby("major")["exam_score"].mean().idxmax()
print("best perfoming major:", best_major)

# TODO: Calculate the correlation between hours_studied and exam_score
corr = df["hours_studied"].corr(df["exam_score"])
print("correlation ( hours studeid vs exam score): ", corr)

# TODO: Create a new column 'performance' with categories:
#       'Excellent' (>90), 'Good' (80-90), 'Average' (70-80), 'Needs Improvement' (<70)
def  perfomance(score):
    if score > 90:
        return "EXcellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    else:
        return "Needs Improvement"
    
df["performance"] = df["exam_score"].apply(perfomance)

print(df["performance"].value_counts())

# Task 3: Advanced Analysis (10 points)
# TODO: For each major and year combination, calculate:
#       - Number of students
#       - Average exam score
#       - Average hours studied
summary = df.groupby(['major', 'year']).agg(
    num_students=('student_id', 'count'),
    avg_exam_score=('exam_score', 'mean'),
    avg_hours_studied=('hours_studied', 'mean')
)

print(summary)
# TODO: Identify top 5 students based on exam_score (handle ties appropriately)
top_students = df.sort_values('exam_score', ascending=False).head(5)
print(top_students[['student_id', 'major', 'exam_score']])

# TODO: Create a pivot table showing average exam_score by major (rows) and year (columns)
pivot = pd.pivot_table(
    df,
    values='exam_score',
    index='major',
    columns='year',
    aggfunc='mean'
)

print(pivot)