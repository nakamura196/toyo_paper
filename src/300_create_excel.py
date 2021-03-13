
import numpy as np
import math
import sys
import argparse
import json
import html
import requests
import os
from bs4 import BeautifulSoup
import csv
import pandas as pd
import glob
import csv

path = "data/中国古籍修復紙譜（上）.xlsx"

df_item = pd.read_excel(path, sheet_name="Sheet1", header=None, index_col=None, engine="openpyxl")

r_count = len(df_item.index)
c_count = len(df_item.columns)

rows = []
rows.append(["dcterms:identifier", "dcterms:title", "dcterms:relation ^^resource", "paper:bunkenmei", "paper:bunrui", "paper:material", "paper:person", "paper:date"])

for j in range(1, r_count):

    print(str(j)+"/"+str(r_count))

    value = df_item.iloc[j, 0]

    print(value)

    id0 = df_item.iloc[j, 2]
    title = id0+df_item.iloc[j, 4]
    date = df_item.iloc[j, 13]
    date = date if not pd.isnull(date) else ""
    rows.append([id0, title, "", df_item.iloc[j, 0], df_item.iloc[j, 1], df_item.iloc[j, 5], df_item.iloc[j, 12], date])

    for i in range(0, 5):
        id = df_item.iloc[j, 7 + i]
        print(id)

        rows.append([id, title+" 観察ポイント{}".format(i+1), id0, "", "", "", "", ""])

    print("---------")

    # break

with open('data/output.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows)

files = glob.glob("../docs/files/large/*/*/*/*.jpg")

rows = []
rows.append(["Item", "Media Url", "dcterms:title", "dcterms:extent"])

map = {}

for file in sorted(files):
    local = file.split("/large/")[1]
    url = "https://diyhistory.org/tmp/paper/" + local

    print(local.split("/"))

    id = local.split("/")[2]

    if id not in map:
        map[id] = {}

    filename = local.split("/")[-1]
    r = int(filename.split("×")[1].split("-")[0])

    if r not in map[id]:
        map[id][r] = []

    map[id][r].append({
        "url": url,
        "title" : filename.split(".")[0]
    })

    print(id)

for id in map:
    for r in sorted(map[id]):
        arr = map[id][r]
        for obj in arr:
            rows.append([id, obj["url"], obj["title"], r])

    # break

with open('data/media_new2.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows)
