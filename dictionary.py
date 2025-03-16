# dictionary 

std = {"std1": "IT", "std2": "CSE", "std3": "ECE", "std4": "EEE", "std5": "MECH"}
print(std["std3"])
print("std1" in std)
print("std2" not in std)


dic = {"Queen": "Bohemian Rhapsody", 
       "Bee Gees": "Stayin' Alive", 
       "U2": "One", 
       "Michael Jackson": "Billie Jean", 
       "The Beatles": "Hey Jude", 
       "Bob Dylan": "Like A Rolling Stone"}
print(len(dic))


# .keys, .values, .items methods:

for key in dic.keys():
    print(key)
    
print(dic.values())

for key, values in dic.items():
    print(key, values)
    
    
if "Promise of the Real" in dic:
    print("key is found")
    
else:
    print("key is not found")
    
    
    