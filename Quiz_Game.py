print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

score = 0

if playing.upper() != "YES":
    quit()

print("Okay! Let's play :) ")
        #@Question 1

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
        #@Question 2

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
        #@Question 3
answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
        #@Question 4

answer = input("What does IS stand for? ").lower()

if answer == "Information security":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
        #@Question 5

answer = input("What does PSU stand for? ").lower()

if answer == "power supplying unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

print("You got "+str(score)+" questions correct!")
print("You got "+str((score/5)*100)+"%.")


