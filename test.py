import sys
from random import randint

print("最小数(n)を入力してください:n ")
n=int(input())
print("最大数(m)を入力してください:m ")
m=int(input())

print("10回以内で回答してください")
n=10
while(n>0):
    num=randint(n,m)
    print("好きな数を入力してください")
    num_user=int(input())
    if num_user==num:
        print("正解です")
        break
    else:
        print("間違っています")
        n-=1
        continue
