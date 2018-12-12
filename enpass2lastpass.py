# enpass2lastpass
# Copyright (c) 2018 Robert Roland
# MIT license

import sys
import csv

if len(sys.argv) < 3:
    print("""
usage:

    enpass2lastpass.py <input file> <output file>
    """)
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

data = []

field_conversions = {
    'username': 'username',
    'login': 'username',
    'email': 'username',
    'password': 'password',
    'url': 'url'
}

with open(infile, 'r') as efile:
    reader = csv.reader(efile)
    next(reader) # skip the header row
    for row in reader:
        title = row[0]
        fields = row[1:len(row)]

        # transform

        converted = {
            'name': title
        }

        name = ''
        if len(fields) == 1:
            # this is a "secure note"
            converted['url'] = "http://sn"
            converted['extra'] = fields[0]
            data.append(converted)
            continue
            
        skip = False
        for i, field in enumerate(fields):
            if (i+1) % 2 == 1:
                name = field.lower()
            else:
                if not name in field_conversions:
                    print('unknown type ' + name + ', skipping row')
                    skip = True
                else:
                    converted[field_conversions[name]] = field

        if not skip:
            if 'url' not in converted:
                converted['url'] = 'http://sn'
            data.append(converted)

with open(outfile, 'w') as lfile:
    fieldnames = ['url','type','username','password','hostname','extra','name','grouping']
    writer = csv.DictWriter(lfile, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    
    for row in data:
        writer.writerow(row)
