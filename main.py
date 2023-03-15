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
def log(msg,lvl=0):
    if "-d" not in sys.argv:
        return
    from clrprint import clrprint
    if lvl==0:
        clrprint(msg,clr='g')
    elif lvl==1:
        clrprint(msg,clr='y')
    elif lvl==2:
        clrprint(msg,clr='r')
    else:
        clrprint(msg,clr='p')
def user(inp,how_just=False,rate_just=False,round_value=3):
    inp=inp.lower()
    log(inp)
    b=t(inp)
    corrected=b.correct().replace("'","")
    log(str(corrected))
    cwords=words.WordMaths(corrected)
    robot=""
    greetings=["hello","hi","morning","hullo","sup","whats good"]
    if [ele for ele in greetings if(ele in corrected)]: # check if any of greetings in c
        log("greeting")
        robot=random.choice(greetings) # greet user
    elif "sentiment" in corrected:
        log("sentiment")
        robot=sentiment(inp,True)
    elif "how are you" in corrected:
        log("how are you")
        choices=["Great","Awful","Fabulous","All the better seeing you"]
        robot=random.choice(choices)+", how about you?"
        how_just=True
    elif how_just==True:
        log("how are you - response")
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
        log("regex maths")
        # regex from https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
        y=words.WordMaths(str(corrected))
        try:
            y.check()
            if y.maths()[0]!=y.maths()[1]:
                robot=y.maths()[0]+'='+y.maths()[1]
        except:
            pass # proceed to next checks
    if corrected=="rate":
        log("rate part1")
        rate_just=True
        robot="Ok, which movie should I rate?"

    elif rate_just==True:
        log("rating movie input")
        y=words.Movie(str(corrected))
        response=y.alli()[0]
        rating_raw=y.alli()[1]
        res2=['That movie was good.','A great title!','Personally, I loved it.']
        res1=['It was ok.','I\'ve seen better.','Pretty good...']
        res0=['Wow, that was awful.','Not worth the ticket.','I hated it!']
        if response==2:
            robot=random.choice(res2)+f" It recieved {rating_raw}/10 on IMDb"
        elif response==1:
            robot=random.choice(res1)+f" It recieved {rating_raw}/10 on IMDb"
        elif response==0:
            robot=random.choice(res0)+f" It recieved {rating_raw}/10 on IMDb"
        else: #error handling
            concat=res2+res1+res0
            robot=random.choice(concat)
        rate_just=False
    else:
        log("else condition")
        qs=['how','what','who','when','where','why','?','is there']
        if [q for q in qs if(q in corrected)]: # check if q is question
            log("google")
            arg=scrape.Search(str(corrected))
            arg.search()
            z=arg.first
            z=z.replace("\\xa0","").replace("...","")
            z=z.replace("?",".").replace("!",".")
            if robot=="":
                robot=z.split(".")[0].strip()
        else:
            log("else",1)
            from semantic3.units import ConversionService
            service = ConversionService()
            try:
                #using raw inp so 'kg' and the like arent corrected
                answ=str(service.convert(str(inp))).replace("'","").replace("(","").replace(")","").split(" ")
                robot=str(round(float(answ[0]),round_value))+answ[1]
                log("successful unit conversion")
            except:
                try:
                    from mathparse import mathparse
                    robot=str(round(mathparse.parse(inp),round_value))
                    log("successful maths equation")
                except:
                    if robot=="":
                        log("sentiment from else",2)
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
        else:
            nextrate=False
        if take['how_just']==True:
            nexthow=True
        else:
            nexthow=False
        print(take["response"])
chat()
