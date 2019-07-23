# coding: utf-8
def P(n):
    print("情書產生器")
    word1=["我","我的","妳","妳的","手裡的"]
    word2=["心","日子","雨","風","天空","雲","等待","哭泣","戀愛","相遇","分離","忘記","靈魂","停止","思念"]
    word3=["溫柔","心醉","驀然","吹過"]
    a=sample(word1,n)
    b=sample(word2,n)
    c=sample(word3,n)
    for i in range(n):
        sentance = [a[i],b[i],c[i]]
        print(" ".join(sentance))
P(3)
