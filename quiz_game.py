print('Welcome to my computer quiz!')

playing = input('do you want to play my game? ')

'''
if playing == 'yes':
    print ('Lest begin!')
else:
    print ('see you another time!')
    quit()
'''

if playing != 'yes':
    print('see you another time!')
    quit()

print ('lets beging!')

answer = input('What does CPU stand for?')
if answer == 'central processing unit':
    print('Correct!')
else:
    print ('wrong answer!')

