# fakturuj_pyco
Generuje faktury z jsonu, pyco. 

Vyhody:

1. Muzes to editovat v oblibenem editoru. 
2. Je to zadarmo. 
3. Jestli se ti to nelibi tak ti furt zustane json soubor. 

Jo a sorry za nazev, ale vzdycky kdyz jsem neco fakturoval tak jsem u toho hrozne nadaval. 

Jak to nainstalovat? 
====================

```
$ pip3 install fakturuj_pyco --user
$ sudo apt-get install wkhtmltopdf
``` 



Jak to pouzivat?
================

```
$ fakturuj 2016_01.json 
```

Tohle vygeneruje pdfka s fakturama do aktualni slozky. Koukni se do slozky ``examples``.


Priklad faktury:
================


```
{
      "number": "2016/01",
      "ico": "00029947",
      "due_days": 15,
      "date": "5.3.2016",
      "currency": "eur",
      "item_list": [
        {
          "title": "Fakturování v Excelu",
          "amount": 20,
          "cost": 150
        },
      ]
}
```

``date`` je optional, lze pouzit libovolnej format ktery rozparsuje ``dateutil``.
``ico`` parameter odkazuje na toho komu fakturujete, vsechny ostatni data
se vytahnout z Aresu. 


helf
====

```
usage: fakturuj [-h] [-o OUTPUT] [-t TEMPLATE] [-i INFO_FILE] json_file

Bleju faktury z jsonu.

positional arguments:
  json_file             jmeno souboru kde mas json

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        kam to chces prdnout.
  -t TEMPLATE, --template TEMPLATE
                        vlastni jinja2 template na generovani faktury.
  -i INFO_FILE, --info_file INFO_FILE
                        soubor z informacema o tobe
```