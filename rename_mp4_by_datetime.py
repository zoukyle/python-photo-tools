#!/usr/bin/python

import argparse

import sys
import os
import datetime
import time

import base
import flags

parser = argparse.ArgumentParser(parents=[flags.common_parser])
args = parser.parse_args()


class RenameMP4ByCreationDateTime(object):
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
            if not eachfile.lower().endswith('mp4'):
                continue

            old_file_path = os.path.join(folder, eachfile)
            file_modified_time = datetime.datetime.fromtimestamp(
                os.path.getmtime(os.path.join(folder, eachfile)))
            new_file_name = 'VID_{}.mp4'.format(
                file_modified_time.strftime('%Y%m%d_%H%M%S'))
            new_file_path = os.path.join(folder, new_file_name)
            print('Rename %s -> %s' % (old_file_path, new_file_path))
            if not args.dry_run:
                os.rename(old_file_path, new_file_path)


if __name__ == '__main__':
    base.main(args.folder, RenameMP4ByCreationDateTime())
