# -*- coding: utf-8 -*-
#original_list=[]

#读取 report.txt 文件中的成绩
first_result=[] #建立空列表，储存第一个结果
with open('report.txt')as f:
    original = f.readlines()#readlines 函数一次读完整个文件，且每行作为一个元素存入列表中
#统计每名学生总成绩、计算平均并从高到低重新排名；
for i in original[1:]:#第一行是课程名称，要先排除第一行的信息，否则会报错
    scores=i.split()#将字符串转化为列表
    psum=0
    subject=0
    for j in scores[1:]:#读取每个学生每一项成绩，第一项是学生名字，所以从第二项开始
        subject+=1#每读一项成绩科目数量+1
        psum+=int(j)#int(j) #把字符串转换成整数，使其能够进行运算
    paverage=psum/subject#计算每个学生的平均分
    paverage1='%.1f'%paverage#将结果保留一位小数
    scores.append(str(psum))#将总分转化为字符串类型并添加到列表中
    scores.append(str(paverage1))#将平均分转化为字符串类型并添加到列表中
    first_result.append(scores)#将添加了总分和平均分的新列表添加到空列表里
    first_result=sorted(first_result,key=lambda x:x[11],reverse=True)#根据平均分进行逆向排序
    #first_result.sort(first_result,key=lambda x:x[11],reverse=True)
#print(first_result)

#汇总每一科目的平均分和总平均分；
second_result=['0','average']#建立新列表储存第二个结果
second_result1=first_result#获取现有的数据
for b in range(1,12):#左闭右开，从1到11，代表读取每个学生11项成绩
    student = 0
    subjectsum = 0
    for a in second_result1:
        student+=1#读取科目总成绩的时候一个一个学生读，每读一次学生数加一
        subjectsum+=float(a[b])#a[b]代表第a个学生第b项成绩
    saverage=subjectsum/student#计算每个科目的平均分
    saverage1='%.1f'%saverage#将结果保留一位小数
    second_result.append(str(saverage1))#将结果转化为字符串，并且保存在之前建立的列表中
#print(second_result)

#添加名次，替换60分以下的成绩为“不及格”
head=['ranking', 'name', 'Chinese' ,'math', 'English', 'physics', 'Chemistry', 'Biology','politics', 'History', 'Geography' ,'totalscore' ,'averagescore']
student1=0
for l in first_result:
    student1+=1#用学生数量作为序号添加到每个学生的列表开头
    l.insert(0,str(student1))#insert代表在列表指定位置添加，将学生数目转化为字符串然后添加到列表最前面
    #print(l)
    lst=2#从每个列表的第二列开始读取成绩【第0列是序号，第1列是学生姓名】
    for m in l[2:-2]:#从每个列表的第二项读到倒数第三项
        if int(m)<=60:
            l[lst]='fail'
            lst+=1
        else:
            lst+=1
first_result.insert(0,second_result)#添加第二个结果
first_result.insert(0,head)#添加表头
#print(first_result)

#将处理后的成绩另存为一个新文件
with open('newfile4.txt', 'w')as w:
    for final in first_result:
        final_result=' '.join(final)+'\n'#将列表转化为字符串，并且用空字符连接
        #print(final_result)
        w.writelines(final_result)#with放在循环外面，文件一直是打开状态，只要一行行往新文件里写入就可以了，如果用with语句，不需要close文件


