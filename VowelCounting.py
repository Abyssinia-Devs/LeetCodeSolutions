count=0
while True:
  print('1.Enter the word.')
  print('0.Exit')
  choice=int(input(' your choice:__'))
  if choice==1:
      count=0
      user_word=input("word:__").lower().strip()
      for letters in user_word:
          if letters in {'a','e','i','o','u'}:
             count+=1
      print(f'There are {count} vowel letters.')
             
  elif choice==0:
      print('GoodBye!.')
      break
  else:
      print('Invalid Option try')
