import math


def calculate_length(point1, point2):
    return math.sqrt(math.pow((point2['x'] - point1['x']), 2) + math.pow((point2['y'] - point1['y']), 2))


point1 = {
    'x': 5,
    'y': 6
}
point2 = {
    'x': 8,
    'y': -1
}
print("Length of line: ", calculate_length(point1, point2))
line1 = {
    'point1': point1,
    'point2': point2
}
line2 = {
    'point1': point2,
    'point2': point1
}
length_of_line1 = calculate_length(line1['point1'], line1['point2'])
length_of_line2 = calculate_length(line2['point1'], line2['point2'])

if length_of_line1 == length_of_line2:
    print("Line1 and Line2 lengths are equal")
elif length_of_line1 > length_of_line2:
    print("Line1's length is greater than that of Line2")
else:
    print("Line2's length is greater than that of Line1")
