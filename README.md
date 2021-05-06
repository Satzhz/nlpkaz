# nlpkaz
WP3. Development NLP tools
1.2. Information for the end users 
1.2.1. Software and hardware requirements 
Software requirements: 
- recent OS released during last 5 years (Windows 10)
- Python 3.6+ 
- libraries: NLTK, Apertium-APy, requests-html, jupyter, numpy, matplotlib, pandas, spacy
- SQLite, Django, Docker Desktop 
Hardware requirements: 
- hardware capable of running recent OS Windows 10

How to use the monolingual NLP tools
Repository consist following directories:
preprocess/ - in the folder consist modules for text preprocessing 
templates/ - in the folder consist modules for morphological analysis, search (words or collocation)
db.sqlite3 - database of fragment texts (save preprocessed: tokens, wordform, pos-taggs parts of speech, etc.) and a list of users (linguists)
files/ - scripts used for web design of html files
