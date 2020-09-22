import sys
import csv
import urllib.request, json
import argparse

flg = True
page = 1

fo = open("data/ids.csv", 'w')
writer = csv.writer(fo, lineterminator='\n')
writer.writerow(
    ["dcterms:identifier","OmekaID"])

while flg:
    url = "https://diyhistory.org/toyo/toyo2/api/items?page=" + str(page)
    print(url)

    page += 1

    response = urllib.request.urlopen(url)
    response_body = response.read().decode("utf-8")
    data = json.loads(response_body.split('\n')[0])

    if len(data) > 0:
        for i in range(len(data)):
            obj = data[i]

            omeka_id = obj["o:id"]

            id = omeka_id
            if "dcterms:identifier" in obj:
                id = obj["dcterms:identifier"][0]["@value"]

            writer.writerow([id, omeka_id])

    else:
        flg = False

fo.close()