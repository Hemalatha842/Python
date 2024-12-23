# Ways to resolve float approximate error

# Using round() function
ex1 = (16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39)
print(round(ex1, 2))

# Using intergers 
ex2 = ((1668 + 698 + 1678 + 1526 + 300 + 439) / 100 )
ex3 = ((16.68*100 + 6.98*100 + 16.78*100 + 15.26*100 + 3.00*100 + 4.39*100) / 100)
print(ex2)
print(ex3)