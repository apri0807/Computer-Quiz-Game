print("Welcome !\n To Computer Quiz")

ask = str(input("Do you want to play:- "))

if ask.lower() != "yes":
    quit()

score = 0

answ = str(input("What does CPU stand's for:- "))
if answ.lower() == "central processing unit":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
    print(f"Your score is {score}")
    quit()

answ = str(input("What does GPU stand's for:- "))
if answ.lower() == "graphic processing unit":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
    print(f"Your score is {score}")
    quit()


answ = str(input("What does RAM stand's for:- "))
if answ.lower() == "random acess memory":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
    print(f"Your score is {score}")
    quit()

answ = str(input("What does WHO stand's for:- "))
if answ.lower() == "world health organtization":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
    print(f"Your score is {score}")
    quit()

answ = str(input("What does GOAT stand's for:- "))
if answ.lower() == "greatest of all time":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
    print(f"Your score is {score}")
    quit()

print(f"Your score is {score}")