class WordMaths:
    def __init__(self,c):
        self.c=c
        self.ans=""
    def check(self):
        for a in self.c.words:
            try:
                self.ans=eval(a)
                self.expr=a
                break
            except:
                pass
        if self.ans!="":
            return True
    def maths(self):
        return [self.expr,self.ans]