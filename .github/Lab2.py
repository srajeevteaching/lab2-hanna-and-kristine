# Team member: Hanna Magan and Kristine
# Course: CS151, Dr.Rajeev
# Date: 22 September 2021
# Programing Assignment 1
# import math
# Program Inputs: ask user for population (births,deaths and migration by year)
birth = float(input("Enter_births"))
deaths = float(input("Enter_death"))
migration = float(input("Enter _migration"))
current_population= float(input("Enter _current_population"))
year = float(input("Enter_year"))
# Program Outputs: ask user for current population
total_population = float(31536000*(year*(birth - deaths + migration))) + current_population
print(total_population)