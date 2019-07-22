#!/usr/bin/python

import argparse

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
import datetime
import time

import base
import flags

parser = argparse.ArgumentParser(parents=[flags.common_parser])
args = parser.parse_args()


class RenamerByDateTime(object):
    """The class to rename image files based on the date time when the image was
    taken."""

    def run(self, folder):
        """Runs the functions to rename files.

        Args:
          folder: str, the folder name.
        """
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
            datetime_obj = datetime.datetime.strptime(timestamp,
                                                      '%Y:%m:%d %H:%M:%S')
            timestamp = time.mktime(datetime_obj.timetuple())
            # if eachfile.lower().startswith('641d'):
            #   timestamp += 300

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
                print('Rename %s -> %s' % (old_jpg_name, new_jpg_name))
                old_cr2_name = '%s.CR2' % old_name
                new_cr2_name = '%s.CR2' % new_name
                print('Rename %s -> %s' % (old_cr2_name, new_cr2_name))
                if not args.dry_run:
                    os.rename(os.path.join(folder, old_jpg_name),
                              os.path.join(folder, new_jpg_name))
                    os.rename(os.path.join(folder, old_cr2_name),
                              os.path.join(folder, new_cr2_name))
                i += 1


if __name__ == '__main__':
    base.main(args.folder, RenamerByDateTime())
