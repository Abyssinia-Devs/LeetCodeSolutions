name_mark=[]
while True:
    print('**************************************************************************************')
    print("1.To register your name and mark.")
    print('2.To see the highest score.')
    print('3.To exit')
    choice=int (input('Enter your choice here. '))
    print('**************************************************************************************')
    if choice==3:
       print('Good Bye!')
       break
    elif choice==1:
       name=input('what is your name?')
       print('Name registered.')
       mark=float(input('what is your total average mark?'))
       print('mark added.')
       name_mark.append({'mark':mark,'name':name})
    elif choice ==2:
       highest_score=max(mak['mark'] for mak in name_mark)
       for mak in name_mark:
        if mak['mark']==highest_score:
           top_scorer=mak['name']
        print(f"{mak['name']}:{mak['mark']}") 
       print(f'The maximum score is ',highest_score,' by',top_scorer)
    else :
       print("Invalid choice. Try again.")
    
       
      
