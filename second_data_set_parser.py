import csv
from pprint import pprint


fn = 'Fistula_Map_second_dataset.csv'

def main():
    sponsor_rows = [
        'FF','UNFPA','Engender',
        'AMREF','WAHA','MSF',
        'DRI','FfFF','OneByOne',
        'CBM','GFMER','Other'
        ]
    reader = csv.DictReader(open(fn, 'rU'))
    other_sponsors = []
    for i,row in enumerate(reader):
        if row['List Other']:
            sponsors = row['List Other'].split(',')
        else:
            sponsors = []
        other_sponsors = other_sponsors + (row['List Other']).split(',')
        for sponsor_row in sponsor_rows:
            if row[sponsor_row] == '0' or row[sponsor_row] == 0:
                continue
            sponsors.append(sponsor_row)
        count = len(sponsors)
        sponsors = ','.join(sponsors) or '-'
        print '[%(lat)s, %(long)s, "%(sponsors)s",%(count)s],'% {
            'lat':row['Latitude'],
            'long':row['Longitude'],
            'sponsors': sponsors,
            'count': count
        }
    all_sponsors = sponsor_rows + other_sponsors
    all_sponsors = [s.strip() for s in all_sponsors]
    print set(all_sponsors)
    # all_sponsors = ','.join(sponsor_rows)
if __name__ == '__main__':
    main()


