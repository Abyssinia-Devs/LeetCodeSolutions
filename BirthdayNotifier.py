print('*****************************************************************')
print('This is a birthday notifier to check whether today is your birthday.')
print('*****************************************************************')
from datetime import date
birthday=[ ]
Today=date.today()
while True:
    print('1.To enter your name,birthday month and date.')
    print('2.To check if today is your birthday. ')
    print('3.To exit.__')
    choice=int(input('Enter your choice.__'))
    if choice==3:
        print('Thank for using this, for now Goodbye!')
        break
    elif choice==1:
        name=input('What is your name?__')
        month=int(input('Enter your birhtday month .__'))
        day=int(input('Enter the date too.__'))
        birthday.append((name,month,day))
        print('you added name,month and date.') 

    elif choice==2:
        for nam,mont,da in birthday:
            if Today.month== mont and Today.day== da:
                print(f'Today is your birhtday {nam}')
            else: 
                print(f'Today is not your birhtday {nam}.')


print(birthday)