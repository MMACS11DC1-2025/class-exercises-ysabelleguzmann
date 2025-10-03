"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""


#we will be making a data analysis page
#it will use the data that we submitted trhough the survey
#the user input will ask who has which topic in common, have the same answers as whoever

#Data Analysis
#Ysabelle Guzman
#Sep 29 2025

#FILE OPENER
file = open("2.4/responses.csv")
question = input('who are you')
question2 = input("who do you think you have in common with")


#READS THE LINES (RESULTS OF SURVEY)
list = file.read.strip(',')
line = list[8].split(',')
print(line)

#LOOPS FOR EACH LINE IN FILE
for line in file:
    if question in line
        question
        




