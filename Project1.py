# -*- coding: utf-8 -*-
#original_list=[]

#读取 report.txt 文件中的成绩
first_result=[]
with open('report.txt')as f:
    original = f.readlines()
#统计每名学生总成绩、计算平均并从高到低重新排名；
for i in original:
    scores=i.split()
    psum=0
    subject=0
    for j in scores[1:]:
        subject+=1
        psum+=int(j)
    paverage=psum/subject
    paverage1='%.1f'%paverage
    scores.append(str(psum))
    scores.append(str(paverage1))
    first_result.append(scores)
    first_result=sorted(first_result,key=lambda x:x[11],reverse=True)
    #first_result.sort(first_result,key=lambda x:x[11],reverse=True)
#print(first_result)

#汇总每一科目的平均分和总平均分；
second_result=['0','average']
second_result1=first_result
for b in range(1,12):
    student = 0
    subjectsum = 0
    for a in second_result1:
        student+=1
        subjectsum+=float(a[b])
    saverage=subjectsum/student
    saverage1='%.1f'%saverage
    second_result.append(str(saverage1))
#print(second_result)

#添加名次，替换60分以下的成绩为“不及格”
head=['ranking', 'name', 'Chinese' ,'math', 'English', 'physics', 'Chemistry', 'Biology','politics', 'History', 'Geography' ,'totalscore' ,'averagescore']
student1=0
for l in first_result:
    student1+=1
    l.insert(0,str(student1))
    #print(l)
    list=2
    for m in l[2:-2]:
        if int(m)<=60:
            l[list]='fail'
            list+=1
        else:
            list+=1
first_result.insert(0,second_result)
first_result.insert(0,head)
#print(first_result)

#将处理后的成绩另存为一个新文件
for final in first_result:
    final_result=' '.join(final)+'\n'
    #print(final_result)
    with open('newfile2.txt', 'a')as w:
        w.writelines(final_result)
w.close()





















