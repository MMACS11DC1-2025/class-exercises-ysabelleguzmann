"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

judges = ["what do you rate the performance out of 10? ", "with this performance, what is the rating out of 10? ", "what do you think out of 10? ", "how was the overall performance out of 10? ", "please rate out of 10. "]

score = 0

for j in judges:
    rating = float(input(j))
    score += rating

rangeofq = len(judges)
    
print("the total score is " + str(score/rangeofq) )
