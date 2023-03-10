class WordMaths:
    def __init__(self,c):
        self.c=c
        self.ans=""
    def check(self):
        for dfksjagjkfhgasdkjfgkasdjfg in self.c.words: # obscure char to prevent bug
            try:
                self.ans=eval(dfksjagjkfhgasdkjfgkasdjfg)
                self.expr=dfksjagjkfhgasdkjfgkasdjfg
                break
            except:
                pass
        if self.ans!="":
            return True
    def maths(self):
        return [self.expr,self.ans]
import re,string

input = " why 1 +2"
