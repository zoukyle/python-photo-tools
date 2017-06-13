#!/usr/bin/python

import argparse

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
import datetime

parser = argparse.ArgumentParser(
    description='Rename folder pictures by datetime')
parser.add_argument('-f', '--folder', type=str, help='The folder to process')
parser.add_argument(
  '--dry_run',
  dest='dry_run',
  action='store_true',
  help='Dry run without renaming')
parser.add_argument('--nodry_run', dest='dry_run', action='store_false')

def main():
  args = parser.parse_args()
  folder = args.folder

  files = os.listdir(folder)
  hash_table = dict()

  for eachfile in files:
    if not eachfile.lower().endswith('jpg'):
      continue

    # metadata = pyexiv2.ImageMetadata(os.path.join(folder, eachfile))
    # metadata.read()
    img = Image.open(os.path.join(folder, eachfile))
    exif_data = img._getexif()
    timestamp = exif_data[36867]
    if timestamp in hash_table:
      hash_table[timestamp].append(eachfile)
    else:
      hash_table[timestamp] = [eachfile]

  keys = hash_table.keys()
  keys.sort()
  i = 0
  for k in keys:
    for eachfile in hash_table[k]:
      old_name = eachfile.split('.')[0]
      new_name = '%03d_%s' % (i, old_name)
      old_jpg_name = '%s.JPG' % old_name
      new_jpg_name = '%s.JPG' % new_name
      print ('Rename %s -> %s' % (old_jpg_name, new_jpg_name))
      old_cr2_name = '%s.CR2' % old_name
      new_cr2_name = '%s.CR2' % new_name
      print ('Rename %s -> %s' % (old_cr2_name, new_cr2_name))
      if not args.dry_run:
        os.rename(os.path.join(folder, old_jpg_name),
                  os.path.join(folder, new_jpg_name))
        os.rename(os.path.join(folder, old_cr2_name),
                  os.path.join(folder, new_cr2_name))
      i += 1


if __name__ == '__main__':
  main()
