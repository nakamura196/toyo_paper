import os
import argparse
import sys


input_dir = "/Users/nakamurasatoru/git/d_toyo/paper/docs/files/original"
output_dir = "/Users/nakamurasatoru/git/d_toyo/paper/docs/files/tile"
output_path = "convert.sh"

files = os.listdir(input_dir)

f = open(output_path, 'w')

for root, dirs, files in os.walk(input_dir):
    for name in files:
        org_file_path = os.path.abspath(root) + "/" + name
        new_file_path = org_file_path.replace(input_dir, output_dir).split(".")[0] + ".tif"

        new_output_dir = os.path.abspath(root).replace(input_dir, output_dir)


        f.write("if [ ! -e "+new_file_path+" ]; then\n")
        f.write("   mkdir -p '" + new_output_dir + "'\n")
        f.write(
            "   convert '" + org_file_path + "' -define tiff:tile-geometry=256x256 -compress jpeg 'ptif:" + new_file_path + "'\n")
        f.write("fi\n")

f.close()