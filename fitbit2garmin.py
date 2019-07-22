#!/usr/bin/env python

from glob import iglob
import json
import time


def main():
    print('Body')
    print('Date,Weight,BMI,Fat')

    for file in iglob('weight*.json'):
        with open(file) as fp:
            js = json.load(fp)
            for e in js:
                try:
                    fat = e['fat']
                except KeyError:
                    fat = int(0)
            time_formatted = time.strftime(
                '%Y-%m-%d',
                time.strptime(e['date'], '%m/%d/%y')
            )
            print('"{0}","{1:.2f}","{2}","{3:.3f}"'.format(
                time_formatted, e['weight'], e['bmi'], fat))

if __name__ == '__main__':
    main()
