
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

flg = True
page = 1

manifests = []

while flg:
    url = "https://diyhistory.org/toyo/toyo3/api/items?page=" + str(page)
    print(url)

    page += 1

    data = requests.get(url).json()

    if len(data) > 0:
        for i in range(len(data)):
            obj = data[i]

            omeka_id = obj["o:id"]

            if len(obj["o:media"]) == 0:
                continue
            

            id = obj["dcterms:identifier"][0]["@value"]
                

            manifests.append({
                "@id" : "https://diyhistory.org/toyo/toyo3/iiif/2/"+id+"/manifest",
                "@type" : "sc:Manifest",
                "label" : obj["dcterms:title"][0]["@value"]
            })

    else:
        flg = False

collection = {
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "@id": "https://diyhistory.org/toyo/toyo3/iiif/2/collection/2809",
    "@type": "sc:Collection",
    "label": "paper",
    "manifests" : manifests
}

f2 = open("data/collection_2.json", 'w')
json.dump(collection, f2, ensure_ascii=False, indent=4, separators=(',', ': '))