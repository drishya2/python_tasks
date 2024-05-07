mark=int(input('Enter your Marks'))


if mark>=90:
    print("You got an A grade")
elif 80<=mark<90:
    print('You got a B grade')
elif 70<=mark<80:
    print('You got a C grade')
elif 60<=mark<70:
    print('You got a D grade')
elif 50<=mark<60:
    print('you got an E grade')
else:
    print('You failed')