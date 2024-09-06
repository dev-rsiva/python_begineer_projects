

print("Welcome to computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != 'yes' :
    quit()

print("Okay! Lets play")

score=0

answer = input("What is the full form of CPU? ")

if answer.lower() == "central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")


 


answer = input("What is the full form of GPU? ")

if answer.lower() == "graphic processing unit":
    print("correct")
    score+=1

else:
    print("incorrect")



answer = input("What is the full form of PSU? ")

if answer.lower() == "power supply":
    print("correct")
    score+=1

else:
    print("incorrect")

print("you have got " + str(score) + " Questions correct" )
print("you have got " + str(score/3) + "%" )