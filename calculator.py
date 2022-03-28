# Simple Calculator using python

#for addition of 2 numbers
def add(num1, num2):
    return num1 + num2

#for subtraction  of 2 numbers
def sub(num1, num2):
    return num1 - num2

#for multiplication of 2 numbers
def mul(num1, num2):
    return num1 * num2

#for division of 2 numbers
def div(num1, num2):
    return num1 / num2

#options of operations
print('Please select an option:-\n'
      '1. ADD\n'
      '2. Subtract\n'
      '3. Multiply\n'
      '4. Divide')

# taking input from the user for operation selection
select = int(input('Select operation from 1, 2, 3 4 : '))

#taking input for num1 and num2
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))

if select == 1:
    print(num1, ' + ', num2,' = ', add(num1, num2))
elif select == 2:
    print(num1, ' - ', num2, ' = ', sub(num1, num2))
elif select == 3:
    print(num1, ' * ', num2, ' = ', mul(num1, num2))
elif select == 4:
    print(num1, ' / ', num2, ' = ', div(num1, num2))
else:
    print('Invalid Input !!')


'''
Output:

Please select an option:-
1. ADD
2. Subtract
3. Multiply
4. Divide
Select operation from 1, 2, 3 4 : 1
Enter first number : 2
Enter second number : 3
2  +  3  =  5

'''