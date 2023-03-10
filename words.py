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

# if re.match(r"[\w\s]*[\d\+\-\*\/]+[\w\s]*", input): # regex from https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
#     # do whatever you want
#     alpa=list(string.printable)
#     n=string.digits+"/"+"-"+"+"+"*"
#     for y in n:
#         alpa=str(alpa).replace(str(y),"")
#     for x in alpa:
#         input=input.replace(x,"")
#     print(eval(input))