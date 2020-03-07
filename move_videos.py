#!/usr/bin/python
"""A command line tool to move video files from the Pictures folder to the
Videos folder.
"""
import argparse
import datetime
import glob
import os
import sys
import shutil

import base
import file_utils
import flags

parser = argparse.ArgumentParser(
    parents=[flags.common_parser],
    add_help=False,
    description=('Move video files from the Pictures folder to the Videos '
                 'folder.\n'
                 'Usage example:\n'
                 '  move_videos.py -f folder-name (2019-07-21 or "2019-07*")'))
parser.add_argument('--videos_dst_folder',
                    type=str,
                    default='/cygdrive/d/Videos/',
                    help='The videos destination folder.')


class VideosMover(base.ProcessorBase):
    """The class the move videos."""

    def __init__(self, args):
        super(VideosMover, self).__init__(args)

    def run(self, folder):
        """Runs the function to move the videos.

        Args:
            folder: str, the folder name to process.
        """
        files = os.listdir(folder)

        for eachfile in files:
            if (not eachfile.lower().endswith('mov') and
                    not eachfile.lower().endswith('mp4')):
                continue

            # Ensures the folder exists in ~/Videos
            expected_dir = os.path.join(self._args.videos_dst_folder, folder)
            if not os.path.exists(expected_dir):
                os.mkdir(expected_dir)

            new_file_path = os.path.join(expected_dir, eachfile)
            print('moving %s to %s' % (eachfile, new_file_path))
            if not self._args.dry_run:
                shutil.move(os.path.join(folder, eachfile), new_file_path)

        # Delete the folder if it's empty
        self._file_utils.delete_folder_if_empty(folder)



if __name__ == '__main__':
    args = parser.parse_args()
    base.main(args.folder, VideosMover(args))
