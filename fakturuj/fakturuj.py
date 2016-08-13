#!/usr/bin/env python

import argparse
import json
import os

from dateutil.parser import parse as date_parse

YES_OPTIONS = ['jo', 'neasi', 'j', 'y']
NOPE_OPTIONS = ['ne', 'nevim', 'mozna', 'n', 'AAAAAA!!!']


def load_data(filename):
    try:
        with open(filename) as f:
            return json.loads(f.read())
    except json.JSONDecodeError:
        fuckem('Ses posral ne? To neni JSON! '
               'I tvoje mama umi delat lepsi json. To neni tak tezky smrade, '
               'proste tam narvi vsude zavorky a je to v cajku.')


def yesno(question):
    while True:
        r = input(question)
        if r.lower() in YES_OPTIONS:
            return True
        elif r.lower() in NOPE_OPTIONS:
            return False


def ask_stupid_questions():
    print('Sorry sraci, ale beze jmena fakturu nevybleju. ')

    personal_info = {
        'name': input('Jmeno vole: '),
        'phone': input('Telefon: '),
        'email': input('Elektricka adresa: '),
        'dph': yesno('Jses platce dani? '),
        'ico': input('ICO, pyco. '),
        'account': input('Cislo uctu: '),
        'address': [
            input('Ulice: '),
            input('Smerovaci cislo: '),
            input('Mesto / vesnice: ')
        ]
    }

    if personal_info['dph']:
        personal_info['dico'] = input('Jeste DICo. Stoji te to za to?')

    if 'Brno' in personal_info['address']:
        print('Zkurvenej brnak.')
    else:
        print('Diky, pyco.')

    return personal_info


def clean_invoice_data(data):
    """
    Overi ze data maji spravnou strukturu, doplni srajdy z aresu.
    """
    try:
        data['date'] = date_parse(data['date'])
    except:
        fuckem('Zadal si blbe datum ve fakture. ')
    if not data['items']






def fuckem(line):
    print(line)
    exit(1)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bleju faktury z jsonu.')

    parser.add_argument('json_file', help='jmeno souboru kde mas json')
    parser.add_argument('--output', help='kam to chces prdnout.')
    parser.add_argument('--info_file', help='soubor z informacema o tobe',
                        default='./me.json')

    args = parser.parse_args()

    if not os.path.isfile(args.json_file):
        fuckem('{} neexistuje, kokote.'.format(args.json_file))
    if not os.path.isfile(args.info_file):
        print('{} neexistuje, pyco.'.format(args.info_file))
        print('Ten soubor je potreba, tam strkam tvoje data, aby ses nemusel '
              'furt opakovat dokola, to by bylo na hovno. '
              'Ale vis co? Muzeme ten soubor vytvorit spolu. To bude prima '
              'zabava. Ted se te teda budu ptat na nejaky radoby vtipny '
              'otazky, kdyz neco poseres tak to pak muzes opravit v tom '
              'souboru. Super co?')

        with open(args.info_file, 'w') as file:
            info = ask_stupid_questions()
            file.write(json.dumps(info, indent=4))
    else:
        info = load_data(args.info_file)

    if not args.output:
        output_file = os.path.splitext(args.json_file)[0] + '.pdf'
    else:
        output_file = args.output

    invoice_data = clean_invoice_data(load_data(args.json_file))
