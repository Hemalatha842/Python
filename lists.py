# list example

ex_1 = [8, 28.1, True, "hema", [1, 2, 3]]

check_1 = (list("hema"))
print("e" in check_1)
print("l" not in check_1)



# list index and slicing

ex_2 = [[0, 2], [4, 6], [8, 10], [12, 14]]

print(ex_2[0])
print(ex_2[3][1])

ex_3 = ["chair", "table", "desk", "lamp", "bed"]

print(ex_3[-1])
print("Most people own at least " + str(ex_2[0][1]) + " " + ex_3[0] + "s")

ex_4 = [0.98, 8.76, 6.54, 4.32]

print(ex_4[1:])
print(ex_4[1:3])
print(ex_4[:2])


