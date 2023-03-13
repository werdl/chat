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
def user(inp,how_just=False,rate_just=False):
    inp=inp.lower()
    b=t(inp)
    corrected=b.correct().replace("'","")
    cwords=words.WordMaths(corrected)
    robot=""
    greetings=["hello","hi","morning","hullo","sup","whats good"]
    if [ele for ele in greetings if(ele in corrected)]: # check if any of greetings in c
        robot=random.choice(greetings) # greet user
    elif "sentiment" in corrected:
        robot=sentiment(inp,True)
    elif "how are you" in corrected:
        choices=["Great","Awful","Fabulous","All the better seeing you"]
        robot=random.choice(choices)+", how about you?"
        how_just=True
    elif how_just==True:
        if corrected.sentiment.polarity>0.3:
            good=["Aww,fab!","That's great!","Cool","Love to hear it"]
            robot=random.choice(good)
        elif corrected.sentiment.polarity<-0.3:
            bad=["Sorry to hear that","It'll get better!","That's annoying :(",";("]
            robot=random.choice(bad)
        else:
            neut=["Nice","*dramatic moment*","It could go either way","Good"]
            robot=random.choice(neut)
    if re.match(r"[\w\s]*[\d\+\-\*\/]+[\w\s]*", str(corrected)): # checks
        # regex from https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
        y=words.WordMaths(str(corrected))
        try:
            y.check()
            robot=y.maths()[0]+'='+y.maths()[1]
        except:
            pass # proceed to next checks
    if corrected=="rate":
        rate_just=True
        robot="Ok, which movie should I rate?"
    elif rate_just==True:
        y=words.Movie(str(corrected))
        response=y.alli()
        res2=['That movie was good','A great title!','Personally, I loved it']
        res1=['It was ok','I\'ve seen better','Pretty good...']
        res0=['Wow, that was awful','Not worth the ticket','I hated it!']
        if response==2:
            robot=random.choice(res2)
        elif response==1:
            robot=random.choice(res1)
        elif response==0:
            robot=random.choice(res0)
        else: #error handling
            concat=res2+res1+res0
            robot=random.choice(concat)
    else:
        qs=['how','what','who','when','where','why','?','is there']
        if [q for q in qs if(q in corrected)]: # check if q is question
            if "-d" in sys.argv:
                print(corrected) # check for debug
            arg=scrape.Search(str(corrected))
            arg.search()
            z=arg.first
            z=z.replace("\\xa0","").replace("...","")
            z=z.replace("?",".").replace("!",".")
            if robot=="":
                robot=z.split(".")[0].strip()
        else:
            if robot=="":
                robot=sentiment(inp)
    return {"response":f"🤖 -- {robot.strip()}",
            "how_just":how_just,
            "rate_just":rate_just}# we return it like this so that the Flask web app can handle it
print("""
Welcome to my conversational chatbot! Ask it some questions.
Note: It is not designed to operate like GPT-3, rather to talk with you.
Try asking 'how are you'.
Type 'sentiment' to perform sentiment analysis.
How about 'rate' and it will rate your movie (data gleaned from IMDb database)

Example:
😃 -- rate
🤖 -- Ok, which movie should I rate?
😃 -- The Hunger Games
🤖 -- Personally, I loved it
If it doesn't recognise your input, it will return the top Google search response if it is a question
Or else say some ambiguous phrases

It can also evaluate maths problems
""")
def chat():
    nexthow=False
    nextrate=False
    while True:
        inp=str(input("😃 -- "))
        take=user(inp,nexthow,nextrate)
        if take['rate_just']==True:
            nextrate=True
        if take['how_just']==True:
            nexthow=True
        print(take["response"])
# chat()
