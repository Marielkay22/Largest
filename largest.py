def largest(a, b, c):
    if a >= b and a >= c:
        return 'First number is the largest ' + str(a)
    elif b >= a and b >= c:
        return 'Second number is the largest ' + str(b)
    else:
        return 'Third number is the largest ' + str(c)

num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))
num3 = float(input('Enter your third number: '))

result = largest(num1, num2, num3)
print(result)