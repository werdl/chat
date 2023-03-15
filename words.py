import string
import imdb
im=imdb.IMDb()
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
class Movie:
    def __init__(self,moviename):
        self.moviename=moviename
    def search(self):
        result=im.search_movie(self.moviename)
        self.topresult=result[0]['title']
        self.topid=result[0].movieID
    def get(self):
        return {'title':self.topresult,'id':self.topid}
    def rate(self):
        code=self.topid
        series=im.get_movie(code)
        self.toprate=series.data['rating']
        return self.toprate
    def good(self):
        if self.toprate>7:
            return 2
        elif self.toprate>4:
            return 1
        else:
            return 0
    def alli(self): # all in one for ease of use
        self.search()
        self.rate()
        return [self.good(),self.toprate]
# y=Movie("Hunger Games")
# print(y.alli())
