import random
def quiz_question(intext):
    correct = False
    problem = intext.split(",")
    a = int(problem[0])
    b = int(problem[1])
    try:
        answer = input("What is the sum of " + str(a) + " and " + str(b) + "? (Enter 'Q' to quit) \n")
        answer = int(answer)
    except: 
        print("Invalid input, try again")
        return quiz_question(intext)
    if(answer == a + b):
        print("Great job")
        correct = True
    else:
        print("Try again!")
    return correct

score = 0
total = 0
for line in open("in-class/week-6/problems.txt", "r"):
    try:
        if(quiz_question(line)):
            score += 1
    except:
        print("Invalid input, try again")
        continue
    total += 1
print("You scored " + str(score) + " out of " + str(total) + " or " + str(float(score)/float(total)*100.0) + "%")

# 'try' handles potential errors, except runs an alternative to getting an error
# you can make 'except' handle only specific errors (NameError, ValueError, etc)
# useful when you don't know what environment your program will be run in/what's going to happen
# generally only want a page at most of code in a function
# computers are great at integers but suck at fractions, it does approximations with floating points - it's compressing it before doing the math