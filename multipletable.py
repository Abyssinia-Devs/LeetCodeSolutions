print('*****************************************************************************************')
print('This allows you to calculate the multiples of numbers in any range you want.')
print('*****************************************************************************************')
total=0
while True:
 print('\n1. to see the multiple table.')
 print('2.to see the total sum of the multiple.')
 print('0.to exit.')
 choice=int(input('Enter your choice here: ')) 
 
 if choice==0:
   print('Bye!')
   break
  
 elif choice==1:
    user_num=int(input(('Enter the number here:')))
    input_range1=int(input('the first range: '))
    input_range2=int(input('the last range: '))
    for num in range(input_range1,input_range2+1):
     new=user_num*num
     print(user_num,'x',num,'=',new)
 elif choice==2:
    user_num=int(input(('Enter the number here:')))
    input_range1=int(input('the first range: '))
    input_range2=int(input('the last range: '))
    for num in range(input_range1,input_range2+1):
    
     new=user_num*num
     
     print(user_num,'x',num,'=',new)
     total+=new
    print('the total is ',total)
 else:
   print('Enter from the option only.')
  

print('*****************************************************************************************')  