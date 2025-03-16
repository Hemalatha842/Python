# while loop

count = 10

while count >= 1:
    print(count)
    count -= 1
    

# sum of numbers from positive numbers

num = int(input("enter an positive integer "))
num1 = num
sum = 0

while num != 0: 
    sum += num
    num -= 1
print(num1)
print(sum)
   
   

#################################################
# for loop 

word = "hello world"

for char in word:
    print(char)


# find number of characters in the string
# using for loop

char = (input("enter a string "))
sum = 0

for letter in char:
    sum += 1
print(char)
print(sum)


# using while loop

count = 0
index = 0

while index<len(char):
    count += 1
    index +=1
   
print(count)
    
    

