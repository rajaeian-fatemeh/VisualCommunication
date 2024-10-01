import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your Excel file
file_path = "EI-Stats-Review-All-Data.xlsx"

# Read the Excel file, skipping the first two rows to locate the data
df = pd.read_excel(file_path, sheet_name="Primary energy cons - EJ", skiprows=2)

# Set the first column as the index (countries)
df.set_index(df.columns[0], inplace=True)

# Create year labels based on the actual dataset from 1965 to 2023 (59 years)
years = list(range(1965, 2024)) + ["Growth rate per annum 2023", "Growth rate per annum 2013-2023", "Share"]

# Assign the new year labels as column headers
df.columns = years

# Remove any rows where all values are NaN
df = df.dropna(how='all')

# Print the cleaned-up DataFrame
print(df.head())

####### Plotting the trends of primary energy consumption
####### for different countries/regions from 1965 to 2023
# Plotting Trends Over Time
plt.figure(figsize=(14, 8))

# Define regions of interest
countries = ['Total North America', 'Total S. & Cent. America', 'Total Europe',
             'Total Middle East', 'Total Africa', 'Total Asia Pacific', 'Total CIS']

# Plotting
sns.lineplot(data=df.loc[countries, years[:-3]].T)  # Transpose for proper plotting
plt.title("Primary Energy Consumption Trends (1965-2023)")
plt.xlabel("Year")
plt.ylabel("Consumption (Exajoules)")
plt.xticks(rotation=45)
plt.legend(title='Countries/Regions', loc='upper left', labels=countries)  # Add legend with labels
plt.grid()
plt.tight_layout()
plt.show()

