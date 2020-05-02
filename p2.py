# -*- coding: utf-8 -*-
import random
import re
def string():
    str='\nabc\n'
    print 1,str.strip().startswith('a')
    print 2,len(str)
    print 3,'-'.join(['1','2','3']),str.strip()
    input('\n enter!')

def operation():
    print 1, 5/2
    print 2, 5<<2
    print 3, min(5, 9)
    print 4, len([1,2,3])
    print 5, range(2,5,2)
    print 6, dir(list)
    print 7, eval('3+4')
    print 8, chr(97), ord('a')

def controlflow():
    score = 90
    if score>=90:
        print 'A+'
    elif score>=85:
        print 'A'
    else:
        print 'impossible'
    i=0
    # while loop
    while i<0:
        print i
        i+=1
    #for loop
    for i in range(1,20,5):
        if i<5:
            continue
        else:
            print '[',i,']'

def demo_list():
    lista = [1,2,3]
    listb = [4,5]
    lista.extend(listb)
    print 1,lista
    lista.insert(3, 0)
    print 2,lista
    lista.append(9)
    lista.reverse()
    print 3, lista
    lista.sort(reverse=True)
    print 4, lista
    print 5, [0] * 12
    print 6, lista * 2
    tuplea = (1,2,3)
    print 7,tuplea

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def demo_dic():
    dica = {1:'a',2:'b',3:'c'}
    print 1,dica
    print 2,dica.has_key(1)
    print 3,dica.keys()
    print 4,dica.values()
    for key,value in dica.items():
        print "key,value:",key,value
    dicb={'+':add, '-':sub}
    print 5,dicb['-'](1,2)
    del dica[1]
    print dica

def demo_set():
    seta=set(([1,2]))
    setb=set((2,3,4))
    print 1,seta.intersection(setb),seta | setb


class User:
    type='USER'
    def __init__(self, name,id):
        self.name=name
        self.id=id
    def __repr__(self):
        return 'I am '+self.name+' '+str(self.id)

class Admin(User):
    type = 'Admin'
    def __init__(self,name,id,group):
        User.__init__(self,name,id)
        self.group=group
    def __repr__(self):
        return User.__repr__(self)+' '+str(self.group)


class Guest(User):
    type = 'GUEST'
    def __init__(self,name):
        User.__init__(self,name,0)
    def __repr__(self):
        return 'I am guest'

def createUser(type):
    if str(type).lower()=='user':
        return User('u1',1)
    elif str(type).lower()=='admin':
        return Admin('A1',101,'g1')
    else:
        return Guest('G1')

def demo_exception():
    try:
        print 2/1
        raise Exception('err--')
    except Exception as e:
        print 'error:'+str(e)
    finally:
        print 'clean up'


#demo_set()
#print createUser('User')
#print createUser('Admin')
#print createUser('Guest')
#demo_exception();

def demo_random():
    random.seed(1)
    print 1, int(random.random()*100)
    print 2,random.random()
    print 3, random.random()
    print 4, random.choice(range(0,100))
    print 5, random.sample(range(0,50),10)
    a=[1,3,4,6,8]
    random.shuffle(a)
    print a

#demo_random()

def demo_re():
    str='abc123def456ghj789'
    p1 = re.compile('[\d]*')
    print p1.findall(str)
    stre = 'a@163.com;b@qq.com;c@163.com;dd@qq.com'
    p2 = re.compile('[\w]+@[qq|163]+\.com')
    print p2.findall(stre)
    strh = '<html><h>title</h><body>xxxx</body>'
    p3 = re.compile('<h>(\w+)</h><body>(\w+)</body>')
    print p3.findall(strh)

#demo_re()

print random.randint(0,123)