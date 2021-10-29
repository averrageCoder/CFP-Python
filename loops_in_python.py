my_list = ['a', 'b', 'c', 'd', 'e']

for i in my_list:
    print(i, end=" ")

print("\nUsing lowerbound and upperbound: ")
for i in range(1, 5, 1):
    print(my_list[i], end=" ")
    if i == 3:
        break
else:
    print("\nfor loop ended!")

print("\nUsing range: ")
for i in range(len(my_list)):
    print(my_list[i], end=" ")

print("\nUsing while loop: ")
i = 0
while i < 5:
    print(i)
    i = i + 1
else:
    print("While loops else block")
