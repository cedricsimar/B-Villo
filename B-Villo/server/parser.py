# -*- coding: utf-8 -*-

import csv, sys, os, pickle, datetime
import dateutil


def parseDate(str_date):
    assert(len(str_date) == 25)
    pre, utc_offset = str_date.split("+")
    assert(utc_offset == "02:00")
    d = datetime.datetime.strptime(pre, "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(hours = 2)
    return d

if __name__ == "__main__":
    has_header = True
    DATA_PATH = "C://Users/Xanto183/Downloads"
    filepath = os.path.join(DATA_PATH, "stations-villo-disponibilites-en-temps-reel.csv")
    file = open(filepath, 'rb')
    reader = csv.reader(file, delimiter = ";")
    column_ids = (0, 6, 8, 9, 10, 11)
    if has_header:
        next(reader, None)
    for row in reader:
        assert(len(row) == 12)
        data = (
            int(row[0]),
            True if row[6] == "OPEN" else False,
            int(row[8]),
            int(row[9]),
            int(row[10]),
            parseDate(row[11])
        )