# coding: utf-8
from random import randint
def game():
    ans=randint(1,10)
    n=-1

    while n!=ans:
        n=int(input('從1-10猜一個數字：'))
        
        if n>ans:
            print('太大了，請再猜一個數字：')
        elif n<ans:
            print('太小了，請再猜一個數字：')
    else:
        print('恭喜猜對')
    
play=True
while play:
    game()
    print('------------------')
    again=input('要再玩一次?Y,N')
    if again=='n':
        play=False    
