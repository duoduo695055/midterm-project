class medallist:
    #注意int两边是要双划线不是单划线
    def __init__(self,country,gold,silver,bronze):
         self.country=country
         self.gold=gold
         self.silver=silver
         self.bronze=bronze

    def get_place(self,place):
        if place==1:
            self.gold+=1
        if place==2:
            self.silver+=1
        if place==3:
            self.bronze+=1

    @property
    # 装饰器 @property，将这个类方法转成只读的属性，称为属性函数。在调用时像属性一样，无需再加括号
    def medaloutput(self):
        return self.gold+self.silver+self.bronze

    # __str__ 是类的内容方法，用来生成一个可读性好的字符串，可供 print 函数调用
    def __str__(self):
        return '%s: gold:%d,silver:%d,bronze:%d'%(self.country, self.gold, self.silver, self.bronze)
    #字符串格式化，多个变量的时候需要加括号

if __name__ == '__main__':
    # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
    China=medallist('China',26,18,26)
    US=medallist('US',46,37,38)
    UK=medallist('UK',27,23,17)
    China.get_place(2)
    print(China)
    print(China.medaloutput)
    medalrank=[China,US,UK]
    #print(medalrank)
    print('goldrank')
    order_golden=sorted(medalrank,key=lambda x:x.gold,reverse=True)
    #print(order_golden)
    for i in order_golden:
        print(i)
    print('totalrank')
    order_total=sorted(medalrank,key=lambda x:x.gold+x.silver+x.bronze,reverse=True)
    #print(order_total)
    for j in order_total:
        print(j)





