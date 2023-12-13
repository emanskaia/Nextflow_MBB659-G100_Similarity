import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("top_10_percent.csv")

# Assuming the column name is "Similarity"
similarity_column = "Similarity"

# Create a distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(df[similarity_column], kde=True, color="blue")
plt.title("Distribution Plot - Similarity Scores")
plt.xlabel("Similarity Score")
plt.ylabel("Frequency")
plt.grid(True)

# Save the plot to a file (adjust the filename and format as needed)
plt.savefig("distribution_plot.png")

# Display the plot
plt.show()
