#!/bin/python
"""A command line tool to purge raw images which are missing corresponding JPGs.
"""
import argparse
import glob
import os
import sys

import base
import file_utils
import flags

parser = argparse.ArgumentParser(
    parents=[flags.common_parser],
    description=(
        'Purge raw files from the disk if there is not a corresponding '
        'JPG file.\nUsage example:\n'
        '  purge_raw.py -f folder-name (2019-07-21 or "2019-07*")'))
args = parser.parse_args()


class RawFilePurger(base.ProcessorBase):

    def run(self, folder):
        jpg_files = glob.glob('%s/*.JPG' % folder)
        if not os.path.exists(folder):
            print('Folder %s does not exist.' % folder)
            sys.exit(1)

        raw_file_extensions = ['CR2', 'ARW']
        delete_files = []
        for jpg_file in jpg_files:
            ####UPDATE
            print(jpg_file)
            stem_name = os.path.basename(jpg_file)
            if stem_name.startswith('C') and len(stem_name.split('T')) == 2:
                delete_files.append(jpg_file)

        for raw_file_extension in raw_file_extensions:
            raw_files = glob.glob('%s/*.%s' % (folder, raw_file_extension))
            for raw_file in raw_files:
                filename_base = raw_file.split('.%s' % raw_file_extension)[0]
                if ('%s.JPG' % filename_base in jpg_files or
                        '%s.jpg' % filename_base in jpg_files):
                    continue
                delete_files.append(raw_file)
        if not delete_files:
            print('No RAW file was deleted')
        else:
            user_input = raw_input(
                'The following RAW files will be deleted:\n%s\n?' %
                '\n'.join(delete_files))
            if user_input == 'y':
                for delete_file in delete_files:
                    print('%s deleted' % delete_file)
                    os.remove(delete_file)
            else:
                print('No RAW file was deleted')
        if not os.path.exists('%s/meta.txt' % folder):
            print('!!!WARNING: NO meta.txt FILD FOUND. MUST CREATE ONE!!!')


if __name__ == '__main__':
    base.main(args.folder, RawFilePurger())
