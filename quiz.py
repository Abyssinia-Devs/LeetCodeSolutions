score_correct=0
score_wrong=0
questions={
    '1.what is the capital city of Ethiopia?':'Adissababa',
    '2.Who is the prime minister of Ethiopia?':"Abiyahmed",
}
print('\n1.To start the question')
print('2. To quit.')
choice=int(input('Enter your choice here. '))
if choice==1:
    print(list(questions.keys())[0])
    try1=input('Guess: ').lower()
    if try1==list(questions.values())[0].lower():
        print('you got the answer.🏆')
        score_correct+=1
    else:
        print('incorrect.')
        score_wrong+=1
        print('The correct answer is ',list(questions.values())[0])
    print(list(questions.keys())[1])
    try2=input("Guess. ").lower()
    if try2==list(questions.values())[1].lower():
        print('correct.🏆')
        score_correct+=1
    else:
        print('incorrect.')
        score_wrong+=1
        print('The correct answer is ',list(questions.values())[1])
elif choice==2:
    print("Don't fear trials.")
    print('Good bye!')
else:
    print('Invalid option.')
print(f'Number of correct:- {score_correct}')
print(f'Number of incorrect:- {score_wrong}')