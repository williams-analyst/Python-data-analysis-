import pandas as pd

# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Score': [85, 92, 78, 90, 88]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Print the full table
print("Student Scores:")
print(df)

# Calculate and print the average score
average_score = df['Score'].mean()
print("\nAverage Score:", average_score)

# Print highest and lowest scores
highest = df['Score'].max()
lowest = df['Score'].min()
print("Highest Score:", highest)
print("Lowest Score:", lowest)
