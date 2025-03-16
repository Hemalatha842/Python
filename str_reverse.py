# reversed string using loop

string  = str(input("Enter a string "))
rev = ""

for char in string:
    rev = char + rev
print(rev)



# reversed string using range

string1 = str(input("enter a string "))
reverse = ""

for char in range(len(string1) -1, -1, -1):
    reverse += string1[char]
print(reverse)

    
    
# word counter

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

def counter(st):
    count = 1
    for word in st:
        if word == " ":
            count += 1
            
    return count

print(counter(str_1))
print(counter(str_2))
print(counter(str_3))
