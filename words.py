class WordMaths:
    def __init__(self,expr,c):
        self.expr=expr
        self.c=c
        self.ans=""
    def check(self):
        for a in self.c.words:
            try:
                self.ans=eval(a)
                break
            except:
                pass
        if self.ans!="":
            return True
    def maths():
        return [self.expr,self.ans]