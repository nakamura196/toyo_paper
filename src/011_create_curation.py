
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

ids = {}

with open('data/ids.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
        ids[row[0]] = row[1]

# --------------

path = "data/中国古籍修復紙譜（上）.xlsx"


df_item = pd.read_excel(path, sheet_name="Sheet1", header=None, index_col=None)

r_count = len(df_item.index)
c_count = len(df_item.columns)

rows = []
rows.append(["dcterms:identifier", "dcterms:title", "class"])

rows2 = []
rows2.append(["dcterms:identifier", "dcterms:relation"])

rows3 = []
rows3.append(["dcterms:identifier", "url", "dcterms:title", "paper:light", "paper:zoom", "paper:depth"])

for j in range(1, r_count):

    print(str(j)+"/"+str(r_count))

    value = df_item.iloc[j, 0]

    print(value)

    ids_arr = []

    for i in range(0, 5):


        row = [df_item.iloc[j, 8 + i], df_item.iloc[j, 7] + " " + "観察ポイント"+str(i+1), "paper:Point"]
        rows.append(row)

        ids_arr.append(ids[df_item.iloc[j, 8 + i]])

    row2 = [df_item.iloc[j, 2], "|".join(ids_arr)]
    rows2.append(row2)

files = sorted(glob.glob("/Users/nakamurasatoru/OneDrive/酉蓮社画像201905-/中國古籍修復紙譜（上）/*/*/*/*.jpg"))

tmp = {}

for file in files:
    print(file)
    id = file.split("/")[-2]
    oid = ids[id]

    url = file.replace("/Users/nakamurasatoru/OneDrive/酉蓮社画像201905-/中國古籍修復紙譜（上）", "https://diyhistory.org/toyo/files")

    if id not in tmp:
        tmp[id] = []
    
    tmp[id].append(url)

for id in tmp:
    arr = tmp[id]

    sorts = ["20", "50", "100", "200", "500", "1000"]

    for s in sorts:
        for url in arr:
            if "×" + s + "-" in url:

                title = "リング片射 " + s + "×"

                type2 = "リング片射"

                depth = ""

                if s in ["500", "1000"]:
                    type2 = "リング照明"
                    title = "リング照明 " + s + "x"
                if "3Dsca" in url:
                    depth = "3Dsca"
                    title += " "+depth
                elif "3D" in url:
                    depth = "3D"
                    title += " "+"3D"
                elif "3to2D" in url:
                    depth = "3to2D"
                    title += " "+"3to2D"
                elif "compo" in url:
                    depth = "COMPO"
                    title += " "+"COMPO"

                rows3.append([id, url, title, type2, s, depth])

with open('data/points.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows)

with open('data/relation.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows2)

with open('data/media.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows3)