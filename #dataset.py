import csv

# Life Expectancy Analyzer

# This program analyzes life expectancy data from a CSV file,
# providing insights into the highest and lowest life expectancy values,
# and calculating the average life expectancy for a user-specified year.

import csv

# Initialize minimum and maximum values
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')

# Initialize corresponding year and country
min_year = ""
min_country = ""
max_year = ""
max_country = ""

# Initialize sum and count for all years
total_life_expectancy = 0
total_count = 0

# Initialize sum and count for specified year
year_life_expectancy_sum = 0
year_count = 0
min_year_life_expectancy = float('inf')
max_year_life_expectancy = float('-inf')
min_year_country = ""
max_year_country = ""

# Import data from CSV file
with open('life-expectancy.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    for row in reader:
        year, country, code, life_expectancy = row
        year = int(year)
        life_expectancy = float(life_expectancy)

        # Update total sum and count
        total_life_expectancy += life_expectancy
        total_count += 1

        # Update minimum value
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_year = year
            min_country = country

        # Update maximum value
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_year = year
            max_country = country

# Display highest and lowest values with year and country
print("# Life Expectancy Overview")
print("-------------------------")
print(f"Lowest Life Expectancy: {min_life_expectancy} years in {min_country} ({min_year})")
print(f"Highest Life Expectancy: {max_life_expectancy} years in {max_country} ({max_year})")
print(f"Average Life Expectancy (All Years): {total_life_expectancy / total_count:.2f} years")
print()

# Prompt user for year
year_of_interest = int(input("Enter the year of interest: "))

# Import data from CSV file again
with open('life-expectancy.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    for row in reader:
        year, country, code, life_expectancy = row
        year = int(year)
        life_expectancy = float(life_expectancy)

        # Check if data belongs to specified year
        if year == year_of_interest:
            year_life_expectancy_sum += life_expectancy
            year_count += 1

            # Update minimum value for specified year
            if life_expectancy < min_year_life_expectancy:
                min_year_life_expectancy = life_expectancy
                min_year_country = country

            # Update maximum value for specified year
            if life_expectancy > max_year_life_expectancy:
                max_year_life_expectancy = life_expectancy
                max_year_country = country

# Check if data exists for specified year
if year_count > 0:
    # Display results
    print(f"# Life Expectancy in {year_of_interest}")
    print("-----------------------------------")
    print(f"Average Life Expectancy: {year_life_expectancy_sum / year_count:.2f} years")
    print(f"Lowest Life Expectancy: {min_year_life_expectancy} years in {min_year_country}")
    print(f"Highest Life Expectancy: {max_year_life_expectancy} years in {max_year_country}")
else:
    print(f"No data found for {year_of_interest}")