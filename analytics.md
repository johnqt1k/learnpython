# Rapport

**Här nedan berättar jag var ifrån jag vill hämta min data**

data = pd.read_csv("johns.csv")

**Här nedan filterar jag min data så att endast person som är över 183 cm visas**

filtered_data = data[data["Height(cm)"] > 183]
print("Filtered data (height > 183):\n", filtered_data)

**Här nedan räknar jag ut personerna som är längre än 183 genomsnittliga längd.**

average_height_per_age = filtered_data.groupby("Age")["Height(cm)"].mean()
print("\nAverage height per age group:\n", average_height_per_age)

**Här nedan skriver jag ut kortast först, längst sist.**

sorted_data = filtered_data.sort_values(by="Height(cm)", ascending=True)
print("\nSorted data by ascending height:\n", sorted_data)

**Här skapas en ny csv fil med den filtrerade datan.**
filtered_data.to_csv("filtered_data.csv", index=False)
