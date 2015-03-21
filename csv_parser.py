import csv
from pprint import pprint


fn = 'DirectRelief_FistulaSurvey_2015_mac.csv'

def main():
    sponsor_rows = [
        'OrgSpons_UNFPA',
        'OrgSpons_FistulaFoundation',
        'OrgSpons_AMREF',
        'OrgSpons_WAHAInt',
        'OrgSpons_Other01',
        'OrgSpons_Other01Text',
        'OrgSpons_EngenderUSAID',
        'OrgSpons_Other02',
        'OrgSpons_Other02Text',
        'OrgSpons_Other03',
        'OrgSpons_Other03Text',
        'OrgSpons_Other04',
        'OrgSpons_Other04Text',
        'OrgSpons_MSF',
        ]
    reader = csv.DictReader(open(fn, 'rU'))
    for i,row in enumerate(reader):
        count = 0
        sponsors = []
        for sponsor_row in sponsor_rows:
            if row[sponsor_row] == 'NULL' or row[sponsor_row] == 0:
                continue
            count += 1
            sponsors.append(sponsor_row[len('OrgSpons_'):])
        sponsors= ','.join(sponsors) or '-'
        print '[%(lat)s, %(long)s, "%(sponsors)s",%(count)s],'% {
            'lat':row['Latitude'],
            'long':row['Longitude'],
            'sponsors': sponsors,
            'count': count
        }
if __name__ == '__main__':
    main()


