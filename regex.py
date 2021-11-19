import re

if __name__ == "__main__":
    pattern1 = "^[A-Za-z]{2,}$"
    name = "Alice"
    if re.fullmatch(pattern1, name):
        print("pattern matched")

    pattern2 = "^([+](91)[\\s])?[0-9]{10}$"
    mobile = "+911234567890"
    if re.fullmatch(pattern2, mobile):
        print("pattern matched")

