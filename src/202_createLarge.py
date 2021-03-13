
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
import shutil

from PIL import Image

# -------------

prefix = "../docs/files/original"

files = sorted(glob.glob(prefix + "/**/*.jpg", recursive=True))

# -------------

for file in files:
    newPath = file.replace(prefix, "../docs/files/large")
    dir = os.path.dirname(newPath)
    os.makedirs(dir, exist_ok=True)
    if not os.path.exists(newPath):
        img = Image.open(file)

        img_resize = img.resize((img.width // 2, img.height // 2))
        img_resize.save(newPath)