## A basic chatbot
### Things it can do
- Do maths problems
- Search google for questions
- convert units
- rate movies
- ask how you are
- greet you
### Ways to access
- Web interface (flask)
- CLI (vanilla Python)
### Known Limitations
- advanced maths operations don't work
- BODMAS/BIDMAS not always applied
- Google scraping a bit vunerable
### Install (OS agnostic)
##### [werdl.onrender.com](werdl.onrender.com)
#### Reqs
- Python
- requirements.txt
```bash
pip install werdl-chat
```
### Get chatting
- New file
```python
from werdl-chat import *
chat()
```

