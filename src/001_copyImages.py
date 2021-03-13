
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

# -------------

prefix = "/Users/nakamurasatoru/OneDrive/酉蓮社画像201905-/中國古籍修復紙譜（上）"

files = sorted(glob.glob(prefix + "/**/*.jpg", recursive=True))

# -------------

for file in files:
    newPath = file.replace(prefix, "../docs/files/original")
    dir = os.path.dirname(newPath)
    os.makedirs(dir, exist_ok=True)
    if not os.path.exists(newPath):
        shutil.copy(file, newPath)