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
import move_videos

parser = argparse.ArgumentParser(
    parents=[move_videos.parser],
    add_help=False,
    description=(
        'Purge raw files from the disk if there is not a corresponding '
        'JPG file.\nUsage example:\n'
        '  purge_raw.py -f folder-name (2019-07-21 or "2019-07*")'))
parser.add_argument('--nomove_videos',
                    action='store_true',
                    help='Also move videos to its own folder.')
parser.add_argument('--force',
                    action='store_true',
                    help='Run without user confirmation.')


class RawFilePurger(base.ProcessorBase):

    def __init__(self, args):
        super(RawFilePurger, self).__init__(args)

    def run(self, folder):
        jpg_files = glob.glob('%s/*.JPG' % folder)
        if not os.path.exists(folder):
            print('Folder %s does not exist.' % folder)
            sys.exit(1)

        raw_file_extensions = ['CR2', 'ARW', 'xmp']
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
            if self._args.force:
                user_input = 'y'
            else:
                user_input = raw_input(
                    'The following RAW files will be deleted:\n%s\n?' %
                    '\n'.join(delete_files))
            if user_input == 'y':
                for delete_file in delete_files:
                    print('%s deleted' % delete_file)
                    if not self._args.dry_run:
                        os.remove(delete_file)
            else:
                print('No RAW file was deleted')

        # Delete the folder if it's empty
        folder_deleted = self._file_utils.delete_folder_if_empty(folder)

        if not folder_deleted and not os.path.exists('%s/meta.txt' % folder):
            print('!!!WARNING: NO meta.txt FILD FOUND. MUST CREATE ONE!!!')


if __name__ == '__main__':
    args = parser.parse_args()
    base.main(args.folder, RawFilePurger(args))
    if not args.nomove_videos:
        base.main(args.folder, move_videos.VideosMover(args))
