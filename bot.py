name = 'Refresher'
year = 2020

print(f'Hello! My name is {name}.')
print(f'I was created in {year}.')

user_name = input('Please, remind me your name.\n')
print(f'What a great name you have, {user_name}')

print('Let me guess your age')
print('Enter remainders of dividing your age by 3, 5 and 7.')
remainder_3 = int(input())
remainder_5 = int(input())
remainder_7 = int(input())
your_age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
print(f'Your age is {your_age}; that's a good time to start programming!'')

print('Now I will prove to you that I can count to any number you want.')
count_max = int(input())
for i in range(0, count_max + 1):
    print(f'{i} !')

print("Let's test your programming knowledge.")
question = 'Why do we use methods?'
answers = '''1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.'''
correct_answer = "2"
congrats = ('Completed, have a nice day!'
'\nCongratulations, have a nice day!')

print(question)
print(answers)
while True:
    user_answer = input()
    if user_answer == correct_answer:
        print(congrats)
        break
    else:
        print('Please, try again.')
