# if, else statements

std_score = int(input("Type the score."))

if std_score >= 90: 
   print("A Grade")
else:
    if std_score >= 80:
        print("B Grade")
    else:
        if std_score >= 70:
            print("C Grade")
        else:
            if std_score >= 60:
                print("D Grade")
            else:
                print("F Grade")
                
                

# elif statement

from random import randint

random = randint(1,10)
print(random)

if random == 1:
    print("I")
elif random == 2:
    print("II")
elif random == 3:
    print("III")
elif random == 4:
    print("IV")
elif random == 5:
    print("V")
elif random == 6:
    print("VI")
elif random == 7:
    print("VII")
elif random == 8:
    print("VIII")
elif random == 9:
    print("IX")
else: 
    print("X")
    

