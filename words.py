import string
class WordMaths:
    def __init__(self,c):
        self.c=c
        self.ans=""
    def check(self):
        alpa=list(string.printable)
        n=string.digits+"/"+"-"+"+"+"*"+"("+")" # one by one as it is list
        for y in n:
            alpa=str(alpa).replace(str(y),"")
        for x in alpa:
            self.c=self.c.replace(x,"")
        try: 
            self.ans=str(eval(str(self.c))) 
            self.expr=str(self.c)
            return True
        except: return False
    def maths(self):
        return [self.expr,self.ans]