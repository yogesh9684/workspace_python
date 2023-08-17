class Father(object):
    def __int__(self,name):
        self.name= name

class Mother(object):
    def __int__(self,fname):
        self.fname = fname

class Baby(Father,Mother):
    def __int__(self):
        Father.__int__(self)
        Mother.__int__(self)


f1 = Father()
f1.name='Yogesh'
f2 = Mother()
f2.fname='Karishma'
print(f1.name , f2.fname)











