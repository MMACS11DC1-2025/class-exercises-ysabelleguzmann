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
first = ""
second = ""

file = open("2.4/responses.csv")

linesofall = file.readlines()

#Now that the file is opened, the user will input their full name
print("HI! I am Botty! Before we begin, can you please state your full name? Thank you :) ")
first_answer = input().strip().lower()

for line_1 in linesofall:
    if first_answer in line_1.lower():
        print("These are your results when we did the survey")
        print(line_1)
        first = line_1

#For here, do the same thing as you did with the first person
print("is there someone you think you will relate with in your Comp-Sci 11 class?")
second_answer = input().strip().lower()

for line_2 in linesofall:
    if second_answer in line_2.lower():
        print("These are your results when we did the survey")
        print(line_2)
        second = line_2

#have the results of the person be split up so that its easier to read in a list
first = first.split(",")
second = second.split(",")

#this code shows the common things between the people
outcome = [item for item in first[2:] if item in second[2:]]

#this just knows how many are in the list
total = len(outcome)

#calucations, so it shows a percent at the end for determination
if len(first) == 0:
    score = 0
else:
    score = total/len(first)*100

    print("You are " +str(score) + " percent alike amongst each other!")

if percent >= 80:
    print("THATS AMAZING!!! I HOPE YOU GUYS ARE FRIENDS :)")
elif percent >= 40:
    print("Hm not too bad honestly")
elif percent >= 10:
    print("so maybe not???")
else:
    print("Yeah so maybe we should stay away from each other...")

                        
        

        




