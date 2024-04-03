import requests
from bs4 import BeautifulSoup
import random
import re

def getinformation():
    # 这是一个简单的爬虫程序
    content = requests.get("http://www.laughfactory.com/jokes").content  # 使用requests库发送GET请求获取网页的内容，将返回的内容赋值给变量content
    soup = BeautifulSoup(content, "html.parser")
    # 将获取到的网页内容传递给BeautifulSoup库的BeautifulSoup函数进行解析。
    # 这里使用了BeautifulSoup(content, "html.parser")来创建一个BeautifulSoup对象，第一个参数是网页内容，第二个参数是解析器类型，这里使用了HTML解析器。
    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())
#一些python的基本操作
def d_string():#字符串功能实例
    str='hellow worD'
    print(str.capitalize()) #首字母转换成大写，其它字母换成小写
    print(str.replace('worD','me')) #替换

def d_operation():#运算符
    print(1+2,5/2,5*2,5-2)
    print(True,not True)
    print(1<2,5>2)
    print(2<<3) #数字2的二进制表示向左移动3位
    print(5|3,5&3,5^3) #或，与，异或

def d_innerfunction():#一些内置函数例子
    print(max(2,1),min(5,3))
    print(len('xxx'),len([1,2,3,]))
    print(abs(-2))
    print(list(range(1,10,2)))
    print(dir(list))
    x=21
    print(eval('x+2'))#将字符串作为 Python 表达式进行求值

#数据结构方面知识
def d_list():#列表
    lista=[1,2,3]
    listb=['a',1,'c',1.1]#python中的列表可以放不同数据类型的变量
    print(1,lista)
    print(2,listb)
    lista.extend(listb)#连接列表
    print(3,lista,len(lista))
    print(4,'a' in lista)
    print(5,lista+listb)
    listb.insert(1,'www')#1为索引
    print(6,listb)
    listb.pop(1)#索引为1的位置弹出去
    print(7,listb)
    listb.reverse()#翻转
    print(8,listb)
    print(9,listb[0],listb[1])
    print(10,listb*2) #连用两次拼车一个列表

def d_dict():#字典
    dicta={1:1,2:4,3:9} #键值对
    print(1,dicta)
    print(2,dicta.keys(),dicta.values())
    for key,value in dicta.items(): #打印字典
        print(3,'键-值',key,'-',value)#键可以是字符串
        print(4,dicta[key]) #通过键获取值
    dicta.pop(1)
    print(5,dicta)

def d_set():#集合
    seta=set((1,2,3))#通过tuple构造集合
    setb=set((2,3,4))
    print(1,seta,type(seta))
    seta.add(4)
    print(2,seta)
    print(3,seta.intersection(setb),seta & setb) #交集
    print(4,seta.union(setb),seta | setb) #并集
    print(5, seta-setb)
    seta.add("x")
    print(seta,len(seta))

#面向对象
class User:#封装
    type='USER'
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def __repr__(self):
        return 'im ' + self.name+' '+str(self.uid)

class Admin(User):
    type = 'ADMIN'
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)#继承
        self.group=group

    def __repr__(self):
        return  'im ' + self.name+' '+str(self.uid)+' '+self.group  #方法重载 (多态)
class Guest(User):
    def __repr__(self):
        return 'im guest ' + self.name+' '+str(self.uid)



def create_user(type):
    if type =='USER':
        return User('u3',3)
    elif type == 'ADMIN':
        return Admin('a2',102,'ad1')
    else:
        return Guest('g1',505)

       #raise  ValueError('error')

#异常处理
def d_error():
    try:#可能出错的代码
        print(2/1)
        print(2/0)
    except Exception as e: #出错以后的处理
        print('error',e)
    finally: #出不出错都要执行的代码
        print("clean up")

#随机数
def d_random():
    #random.seed(1) #指定seed的伪随机，指定seed以后随机数会固定，不固定的话seed随时间变化
    print(1, random.random()) #随机生成0-1之间的浮点数
    print(2, random.randint(0,200)) #0-200的随机整数
    print(3, random.choice(range(0,100))) #0-100之间随机选一个
    print(4, random.sample(range(0,100),4))#0-100之间随机选4个
    a=[1,2,3,4,5,6]
    random.shuffle(a) #将一个列表随机打乱
    print(5,a)

 #正则表达式
def d_re():
    str = 'abdi2342k46558'
    p1=re.compile('\d+') #\d找数字 \D 找非数字 \s 找空格 \w 找词  +至少匹配一次 *可以匹配0次 ？只能匹配0/1次
    p2=re.compile('\d')
    print(1,p1.findall(str))
    print(2,p2.findall(str))
    str2='a@163.com;b@gmail.com;kk@163.com'
    p3=re.compile('[\w]+@[163|qq]\.com') #\.为转义字符  这里是找163或qq邮箱  |为或，^为取反
    print(3,p3.findall(str2))
    str3='<html><h>tittle</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>') #^< 表示不要<开头的
    print(4,p4.findall(str3))
    p5= re.compile('<h>([^<]+)</h><body>([^<]+)</body>') #寻找标题和body ()为要寻找的范围
    print(5,p5.findall(str3))
    str4 = 'xx2024-03-28yy'
    p6 = re.compile('\d+-\d+-\d+')
    p7 = re.compile('\d{4}-\d{2}-\d{2}') #指定次数的表达方式
    print(6,p6.findall(str4))
    print(7,p7.findall(str4))



if __name__ == '__main__': #在运行当前模块时执行一些特定的代码，而在将当前模块作为模块导入到其他模块时不执行这些代码。
    #user1=User('u1',01)#在 Python 中，整数以零开头会被解释为八进制表示
    #user1 = User('u1', 1)
    #user2=User('u2',2)
    #print(user1)
    #admin=Admin('a1',101,'ad1')
    #print(admin)
    #print(create_user("USERS"))#多态
    #d_error()
    #d_random()
    d_re()




