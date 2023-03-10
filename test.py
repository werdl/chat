from textblob import TextBlob
inp="ello ello ello 12+13"
c=TextBlob(inp)
print(c.words)
for a in c.words:
    try:
        ans=eval(a)
        break
    except:
        pass
print(ans)