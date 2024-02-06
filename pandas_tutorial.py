import pandas as pd

# Load data from CSV file
data = pd.read_csv("johns.csv")

# Filter data to include only people with height over 183
filtered_data = data[data["Height(cm)"] > 183]
print("Filtered data (height > 183):\n", filtered_data)

# Calculate average height per age group
average_height_per_age = filtered_data.groupby("Age")["Height(cm)"].mean()
print("\nAverage height per age group:\n", average_height_per_age)

# Sort data by 'Height(cm)' in ascending order
sorted_data = filtered_data.sort_values(by="Height(cm)", ascending=True)
print("\nSorted data by ascending height:\n", sorted_data)

filtered_data.to_csv("filtered_data.csv", index=False)
