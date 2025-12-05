from datetime import date
Today=date.today()
balance=0
trial=0
print(f'----------{Today}-------------')
Pin={
  'kiya':2026,
  'miki':2025,
  'gold':2030,
  'sami':2015
}
user_pin=int(input('Enter your four digit  pin._'))
trial+=1
if user_pin==list(Pin.values())[1]:
   print('welcome miki🤝')
elif user_pin==list(Pin.values())[0]:
   print('welcome Kiya 🤝')
elif user_pin==list(Pin.values())[2]:
   print('welcome gold 👋')
elif user_pin==list(Pin.values())[3]:
   print('welcome sami 😎')
else :
   print('Invalid pin.🤨')
   print(f'you tried {trial}')
while True:
     print('1.Check Balance')
     print('2.Deposit Money')
     print('3. Withdraw Money')
     print('4. Exit')
     choice=int(input('Enter your choice here.__'))
     if choice==4:
      print('GoodBye!.👋👋')
      break
     elif choice==1:
      print(f'Your balance is ${balance}')
     elif choice==2:
      deposit=float(input('Enter the amount to be deposited.__$'))
      balance+=deposit
      if deposit<0:
       print(f"Negative can't be deposited.🤣")
      print(f' you deposited {deposit} amount, Your balance is now ${balance}.')
     elif choice==3:
      withdraw=float(input('Enter the amount to be withdrawal._$'))
    
      if withdraw > balance:
       print(f'You have insufficient funds🥶🥶, your balance is ${balance} but you tried to access ${withdraw} how so? work hard first.😁😁')
      elif withdraw<0:
       print('You should use only postive integers.🎭')
      elif withdraw <=balance:
       balance-=withdraw
       print(f"you credited ${withdraw} ,Your balance is now ${balance}. ")
      else :
       print('Invalid !😁')
     
     else :
      print('Invalid Option.🤨🫠')


print(f'----------{Today}-------------')

