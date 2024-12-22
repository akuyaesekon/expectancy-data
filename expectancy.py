import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Admin/expectancy-data/Life-Expectancy-Data-Averaged.csv")

df

df.head(10)

df.drop_duplicates()

df.fillna(0)

df.head(10)

df.columns

df.head(10)

print("\nFirst 10 rows after removing duplicates and filling missing values:")
print(df.head(10))

first_10_rows = df.head(10)
first_10_rows.to_csv("first_10_rows.csv", index=False)

print("\nFirst 10 rows have been saved to 'first_10_rows.csv'")

# If you want to check the columns in the dataset
print("\nColumns in the dataset:")
print(df.columns)

# Scatter plot: Life Expectancy vs GDP per Capita
df.plot(x='GDP_per_capita', y='Life_expectancy', kind='scatter', alpha=0.6)
plt.title('Life Expectancy vs GDP per Capita')
plt.label('GDP per Capita')
plt.label('Life Expectancy')
plt.show()

# Scatter plot: Infant Deaths vs Life Expectancy
df.plot(x='Infant_deaths', y='Life_expectancy', kind='scatter', alpha=0.6)
plt.title('Infant Deaths vs Life Expectancy')
plt.label('Infant Deaths')
plt.label('Life Expectancy')
plt.show()

# Scatter plot: Alcohol Consumption vs Life Expectancy
df.plot(x='Alcohol_consumption', y='Life_expectancy', kind='scatter', alpha=0.6)
plt.title('Alcohol Consumption vs Life Expectancy')
plt.label('Alcohol Consumption (L per capita)')
plt.label('Life Expectancy')
plt.show()

# Scatter plot: Life Expectancy vs Schooling
df.plot(x='Schooling', y='Life_expectancy', kind='scatter', alpha=0.6)
plt.title('Life Expectancy vs Schooling')
plt.label('Schooling (Years)')
plt.label('Life Expectancy')
plt.show()

# Box plot: Life Expectancy by Economy Status
df.plot(x='Economy_status', y='Life_expectancy', kind='box', patch_artist=True)
plt.title('Life Expectancy by Economy Status')
plt.label('Economy Status')
plt.label('Life Expectancy')
plt.show()

# Line plot: Life Expectancy over Time (example for a country)
df.plot(x='Year', y='Life_expectancy', kind='line')
plt.title('Life Expectancy Over Time')
plt.label('Year')
plt.label('Life Expectancy')
plt.show()

# Bar plot: Average Life Expectancy by Region
df.groupby('Region')['Life_expectancy'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Life Expectancy by Region')
plt.label('Region')
plt.label('Average Life Expectancy')
plt.show()

# Histogram: Distribution of Life Expectancy
df['Life_expectancy'].plot(kind='hist', bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Life Expectancy')
plt.label('Life Expectancy')
plt.label('Frequency')
plt.show()

# Stacked bar plot: Life Expectancy by Region over Time
df.pivot_table(values='Life_expectancy', index='Year', columns='Region').plot(kind='bar', stacked=True, figsize=(14, 7))
plt.title('Life Expectancy by Region Over Time')
plt.label('Year')
plt.label('Life Expectancy')
plt.show()