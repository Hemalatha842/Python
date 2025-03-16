# fizzbuzz proble

nums = range(1, 51)

for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    
    
    
# factorial number


no = int(input("enter a number"))

fact = 1
for i in range(1, no+1):
    fact *= i

print(fact)

