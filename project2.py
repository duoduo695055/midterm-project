# -*-coding:utf-8
from random import randint

username= input('please input your username: ')
print('welcome to the game,',username,',''have a great time!')

try:
    with open('game.txt','r')as f:
        lines=f.readlines()
except:
    with open('game.txt','w+')as f:
        lines=f.readlines()


scores={} #建立空字典，储存所有用户的用户名和用户信息
for l in lines:
    s=l.split()
    scores[s[0]]=s[1:]
score=scores.get(username)
if score is None:
    score=[0,0,0]

periodtime=int(score[0])#记录游戏的轮数
totaltime=int(score[1])#记录总共猜的次数
minwintime=int(score[2])#记录最快猜中次数
if periodtime>0:
    ave=float(totaltime/periodtime)
else:
    ave=0

print('%s you have played this game for %d times'' your quickest wintime is %d times'' your average wintime is %.2f'%(username,periodtime,minwintime,ave))


print('Guess what I think?')
num = randint(1, 100)
times = 0
Bingo=True
while Bingo==True:
    times+=1
    while True:
        print('please input the number from 1 to 100')
        answer = int(input())
        try:
            if answer>100 or answer==0:
                print('please input the number again')
            else:
                break
        except:
                pass
    if answer>num:
            print('too large')
    if answer<num:
            print('too small')
    if answer==num:
        print('bingo')
        periodtime+=1
        totaltime+=times
        if periodtime == 1 or times < minwintime:
            minwintime=times

        print('it is your %d times to play the game' %(periodtime))
        print('you played %d times in all round'%(totaltime))
        print('your quickest wintime is %d times'%(minwintime))
        scores[username]=[str(periodtime),str(totaltime),str(minwintime)]
        result=''
        for l in scores:
            line=l+''+''.join(scores[l])+'\n'
            result=result+line

        with open('game.txt','w')as w:
            w.write(result)

        print('.....................................................')
        newgame=input('if you want to play the game again, please input go')
        if newgame=='go':
            times=0
            num= randint(1, 100)
            print('Guess what I think?')
            Bingo=True
        else:
            Bingo=False

















