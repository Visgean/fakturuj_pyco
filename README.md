# fakturuj_pyco
Generuje faktury z jsonu, pyco. 

Vyhody:

1. Muzes to editovat v oblibenem editoru. 
2. Je to zadarmo. 
3. Jestli se ti to nelibi tak ti furt zustane json soubor. 

Jak:

```
$ fakturuj 2016_01.json 
```

Tohle vygeneruje pdfka s fakturama do aktualni slozky. Koukni se do slozky ``examples``.

Jak to nainstalovat? 

```
$ pip3 install fakturuj_pyco --user
$ sudo apt-get install wkhtmltopdf
``` 


Jo a sorry za nazev, ale vzdycky kdyz jsem neco fakturoval tak jsem u toho hrozne nadaval. 



```
usage: fakturuj [-h] [--output OUTPUT] [--info_file INFO_FILE] json_file

Bleju faktury z jsonu.

positional arguments:
  json_file             jmeno souboru kde mas json

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT       kam to chces prdnout.
  --info_file INFO_FILE
                        soubor z informacema o tobe
```