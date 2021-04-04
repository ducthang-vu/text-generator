# text-generator
**text-generator** is a Python application which generate random text from a corpus of texts from various authors. 
The following author are available:
- [Kapy Perry](corpus/katy_perry): **20 songs**,
- [Lady Gaga](corpus/lady_gaga): **30 songs**, and
- [Saint Paul](corpus/saint_paul): **Letter to the Romans**.


## Minimum requirements 
python 3.9.0

atomicwrites==1.4.0  
attrs==20.3.0  
colorama==0.4.4  
coverage==5.5  
iniconfig==1.1.1  
packaging==20.9  
pluggy==0.13.1  
py==1.10.0  
pyparsing==2.4.7  
pytest==6.2.2  
toml==0.10.2  


## Usage
Open terminal and install the necessary packages by running:

```
pip install -r requirements.txt
```

Then start the application by running from the root directory **main.py**. for example:
The script accepts the following arguments:
- **--author**, **-a**: the author, and
- **--length**, **-l**: the total number of words to be generated

For example:
```
python main.py -a lady_gaga -l 10

fight gotta find your love love again Oh oh Ooh
```

For running unit tests, do:
```
    coverage run -m pytest
    coverage report
    coverage html
```
The latter command create the coverage file **coverage/index.html**, which can be open with a browser.

## Implementation notes ##
This application retrieve a corpus and then generate a [**Markov chain**](https://en.wikipedia.org/wiki/Markov_chain) 
which establishes a relationships between words.

The algorithm is simple and naive: it considers as word any substring between spaces, provided that only letters, 
apostrophes and hyphen are kept. 
Further improvement may be added in the future.