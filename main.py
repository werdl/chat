from textblob import TextBlob as t
import sys,random,re,scrape,words,string
def sentiment(inp,take=False): # Take input 
    if take==True:
        inp=str(input("😃 -- "))
    inp=inp.lower()
    b=t(inp)
    c=b.correct()
    robota=c.sentiment.polarity
    if robota>0.3:
        pos=["Positive vibes, dude! :)",":)","Cool","Positivity rocks!"]
        robot=random.choice(pos)
    elif robota<-0.3:
        neg=["Wow, that's negative!",":O","Calm down dude!","Whoa"]
        robot=random.choice(neg)
    else:
        neu=["Lovely","I see","Ahhhhh","Makes sense"]
        robot=random.choice(neu)
    try:
        if "-d" in sys.argv:
            print(robota)
    except:
        pass
    return robot
def user(inp,how_just):
    inp=inp.lower()
    b=t(inp)
    c=b.correct().replace("'","")
    cwords=words.WordMaths(c)
    greetings=["hello","hi","morning","hullo","sup","whats good"]
    
    if [ele for ele in greetings if(ele in c)]: # check if any of greetings in c
        robot=random.choice(greetings) # greet user
    elif "sentiment" in c:
        robot=sentiment(inp,True)
    elif "how are you" in c:
        choices=["Great","Awful","Fabulous","All the better seeing you"]
        robot=random.choice(choices)+", how about you?"
        how_just=True
    elif how_just==True:
        if c.sentiment.polarity>0.3:
            good=["Aww,fab!","That's great!","Cool","Love to hear it"]
            robot=random.choice(good)
        elif c.sentiment.polarity<-0.3:
            bad=["Sorry to hear that","It'll get better!","That's annoying :(",";("]
            robot=random.choice(bad)
        else:
            neut=["Nice","*dramatic moment*","It could go either way","Good"]
            robot=random.choice(neut)
    elif re.match(r"[\w\s]*[\d\+\-\*\/]+[\w\s]*", str(c)):
        # regex from https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
        alpa=list(string.printable)
        n=string.digits+"/"+"-"+"+"+"*"
        for y in n:
            alpa=str(alpa).replace(str(y),"")
        for x in alpa:
            c=c.replace(x,"")
        robot=str(c)+"="+str(eval(str(c)))
    elif cwords.check()==True:
        robot=cwords.maths()[0]+"="+str(cwords.maths()[1])
    else:
        qs=['how','what','who','when','where','why','?','is there']
        if [q for q in qs if(q in c)]: # check if q is question
            if "-d" in sys.argv:
                print(c) # check for debug
            arg=scrape.Search(c)
            arg.search()
            z=arg.first
            z=z.replace("\\xa0","").replace("...","")
            z=z.replace("?",".").replace("!",".")
            robot=z.split(".")[0].strip()+"."
        else:
            robot=sentiment(inp)
    return [f"🤖 -- {robot.strip()}",how_just]
print("""
Welcome to my conversational chatbot! Ask it some questions.
Note: It is not designed to operate like GPT-3, rather to talk with you.
Try asking 'how are you'.
Type 'sentiment' to perform sentiment analysis.

If it doesn't recognise your input, it will return the top Google search response if it is a question
Or else say some ambiguous phrases

Also please bear in bind the search is unreliable at best (dodgy dependancy)
""")
nexthow=False
while True:
    inp=str(input("😃 -- "))
    take=user(inp,nexthow)
    if take[1]==True:
      nexthow=True
    else:
      nexthow=False
    print(take[0])
