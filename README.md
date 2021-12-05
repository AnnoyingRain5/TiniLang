<h1 align="center">
<p><b>TiniLang</b> - The Victini Programming Language</p>
<br>
<br>
<img style="margin-top:-100px" src="images/victini.gif" />
<br>
</h1>

A fork of PikaLang, which is a [brainfuck][2] derivative based off the vocabulary of [Victini][3] from [Pokemon][4].

Syntax
------
TiniLang  | brainfuck | description                                   
----------|-----------|-----------------------------------------------
`vi`      | +         | increment the byte at pointer                 
`ni`      | -         | decrement the byte at pointer                 
`vicvic`  | [         | if pointer is zero, jump to matching `tinitini`    
`tinitini`| ]         | if pointer is nonzero, jump to matching `vicvic`
`victi`   | >         | increment the data pointer                    
`vicni`   | <         | decrement the data pointer                    
`vic`     | ,         | input of one byte into pointer                
`tini`    | .         | output the byte at pointer                    


Installation
------------
stable:
```shell
pip install TiniLang
```

or bleeding edge...
```shell
git clone https://github.com/AnnoyingRain5/TiniLang.git
cd TiniLang

python setup.py install
```


Usage
-----
```shell
TiniLang path/to/file.tini
```


File Extention
--------------
A TiniLang program must be stored in a file with a `.tini` extention


API Usage
---------
```python
import TiniLang

sourcecode = """
    tinitini vi vi vi vi vi vi vi vi vic vicvic vi vi vi vi vi vi vi vi vi tinitini ni tini vicvic victi tinitini vi vi vi vi vic vicvic vi vi vi vi vi vi vi tinitini ni tini vicvic vi victi vi vi vi vi vi vi vi victi victi vi vi vi victi tinitini tinitini vi vi vi vi vi vi vic vicvic vi vi vi vi vi vi vi tinitini ni tini vicvic vi 
    vi victi ni ni ni ni ni ni ni ni ni ni ni ni victi tinitini vi vi vi vi vi vi vic vicvic vi vi vi vi vi vi vi vi vi tinitini ni tini vicvic vi victi vicvic victi vi vi vi victi ni ni ni ni ni ni victi ni ni ni ni ni ni ni ni victi tinitini tinitini tinitini vi vi vi vi vic vicvic vi vi vi vi vi vi vi vi tinitini ni 
    tini vicvic vi victi  
    """

# or use sourcecode = TiniLang.load_source("FILENAME.tini") to load from file

TiniLang.evaluate(sourcecode)
```

Development
-----------
When developing, use `pipenv` to install needed tools.

```sh
pipenv install

pipenv run black .

pipenv run python -m TiniLang tests/hello-world.tini
```

Thanks
------
Special thanks to [Groteworld][5] for creating pikalang, which was only slightly modified to create TiniLang

Disclaimer
----------
This is a fan-based parody of themes from [Pokemon][3]. The language,
as well as its author, is in no way associated with the Pokémon francise
and its creators, nor is this project, in any way, for-profit.


[1]: http://esolangs.org/wiki/Pikalang
[2]: http://en.wikipedia.org/wiki/Brainfuck "Brainfuck"
[3]: https://www.google.com/search?q=Victini&tbm=isch "Victini"
[4]: http://www.pokemon.com/ "Pokemon"
[5]: https://github.com/groteworld/pikalang "GroteWorld"
