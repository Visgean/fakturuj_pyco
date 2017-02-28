#!/usr/bin/env python

import argparse
import json
import os
import pdfkit

from datetime import timedelta, datetime
from ares_util.ares import call_ares
from dateutil.parser import parse as date_parse
from jinja2 import Environment, PackageLoader, FileSystemLoader


def fuckem(line):
    print(line)
    exit(1)


def load_data(filename):
    try:
        with open(filename) as f:
            return json.loads(f.read())
    except json.JSONDecodeError:
        fuckem('Ses posral ne? To neni JSON! '
               'I tvoje mama umi delat lepsi json. To neni tak tezky smrade, '
               'proste tam narvi vsude zavorky a je to v cajku.')


def ask_stupid_questions():
    ico = input('ICO, pyco. ')
    personal_info = {
        'account': input('Cislo uctu: '),
        'ares': call_ares(ico)
    }

    print('Diky, pyco.')
    return personal_info


def clean_invoice_data(data):
    """
    Overi ze data maji spravnou strukturu, doplni srajdy z aresu.
    """
    if not data.get('date'):
        data['date'] = datetime.today()
    else:
        try:
            data['date'] = date_parse(data['date'])
        except:
            fuckem('Zadal si blbe datum ve fakture. ')
    if not data['item_list']:
        fuckem('Musis vyplnit nejake polozky na fakturu...')
    data['date_due'] = data['date'] + timedelta(days=data['due_days'])

    if 'ico' not in data:
        assert 'company_data' in data, "You have to either specify ICO or company data."
        data['company_data']
    else:
        data['company_data'] = call_ares(data['ico'])
    return data


def render_template(invoice, info, filename=None):
    if filename:
        dir_name, f_name = os.path.split(filename)
        env = Environment(loader=FileSystemLoader(dir_name or '.'))
        template = env.get_template(f_name)
    else:
        env = Environment(loader=PackageLoader('fakturuj'))
        template = env.get_template('invoice.html')

    return template.render(
        invoice=invoice,
        info=info,
        currency=invoice.get('currency', 'Kč'),
        title='Faktura {}'.format(invoice['number']),
        sum_total=sum([i['cost'] * i['amount'] for i in invoice['item_list']]),
        transaction_id=''.join([s for s in invoice['number'] if s.isdigit()]),
        space_number=lambda n: '{:,}'.format(n).replace(',', ' '),
    )


def main():
    parser = argparse.ArgumentParser(description='Bleju faktury z jsonu.')

    parser.add_argument('json_file', help='jmeno souboru kde mas json')
    parser.add_argument('-o','--output', help='kam to chces prdnout.')
    parser.add_argument('-t', '--template',
                        help='vlastni jinja2 template na generovani faktury.')
    parser.add_argument('-i', '--info_file', help='soubor z informacema o tobe',
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

        if input("Chces ho vytahnout z ARESu? Ano/Ne") in ('Ano', 'ANO', 'A', 'a'):
            with open(args.info_file, 'w') as file:
                info = ask_stupid_questions()
                file.write(json.dumps(info, indent=4))
        else:
            fuckem('Budes si ten soubor muset vytvorit sam.')
    else:
        info = load_data(args.info_file)

    if not args.output:
        output_file = os.path.splitext(args.json_file)[0] + '.pdf'
    else:
        output_file = args.output

    invoice_data = clean_invoice_data(load_data(args.json_file))

    html_content = render_template(invoice_data, info, filename=args.template)
    pdfkit.from_string(html_content, output_path=output_file)


if __name__ == '__main__':
    main()