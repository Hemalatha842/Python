# Dictionary methods part1


dic1 = {}.fromkeys("abcdefghijklmnopqrstuvwxyz", "consonant")
print(dic1)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
popped = fast_food_items.pop("McDonald's")
print(popped)

fast_food_items.popitem()
print(fast_food_items)




# Dictionary methods part2

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)

celeb = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(another_one)


