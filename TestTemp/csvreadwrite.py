#! /usr/bin/env python
#encoding=utf-8
#author=zgd

import csv

def readCsvList():
    with open('../TestReport/report.csv','r') as f:
        reader = csv.DictReader(f)
        for i in reader:
            print(dict(i)["rspdesc"])
readCsvList()
















