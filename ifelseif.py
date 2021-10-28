number = 2
if number % 2 == 0:
    print('%d is Even!' % number)
else:
    print('%d is Odd!' % number)

if number < 0:
    print('%d is Negative!' % number)
elif number == 0:
    print('%d is Zero!' % number)
elif number > 0:
    print('%d is Positive!' % number)
else:
    print('%s is not a number' % number)