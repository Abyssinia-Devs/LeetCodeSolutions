# Simple Palindrome Checker Program
# -------------------------------------------------------
# This program allows the user to:
#   1. Enter a word and check if it is a palindrome
#   0. Exit the program
#
# It validates user input so only 1 or 0 are allowed.
# If the user enters text instead of numbers, a warning is shown.
# A palindrome is checked by comparing the string with its reverse.
# *******************************************************
print('************SIMPLE PLAINDROM****************')
while True:
    print('1.Check Word.')
    print('0.Exit')
    choice=input('Enter your choice.__')
    try:
        choice=int(choice)
        if not (choice==1 or choice==0):
         print('Please try to enter 1 or 0 only 🙄🤨')
    except ValueError:
        print("strings are not acceptable , Don't you see what is written.(MELATA)😁😁😁😁")
    if choice==1:
      alphabet=input('Enter the word here.__').replace(" ","").strip()
      if (alphabet[0:])==(alphabet[::-1]):
        print(f'The word {alphabet} is plaindrom.')
      else:
        print(f'The word {alphabet} is not plaindrom.😁')
    elif choice==0:
        print('GoodBye!🤝')
        break

print('**********************************************')
