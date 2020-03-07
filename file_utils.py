#!/usr/bin/python
"""Library class for file utils."""

import glob
import os
import sys


class FileUtils(object):
    """FileUtils class to manage files and folders."""

    def __init__(self, dry_run=False):
        self._dry_run = dry_run

    def get_folders(self, folder_pattern):
        """Gets a list of folders that match the folder_pattern.

        Args:
            folder_pattern: str, can be a specific folder or with '*'

        Returns:
            a list of str.
        """
        if not folder_pattern:
            print('The folder must be set')
            sys.exit(1)

        folders = []
        if '*' in folder_pattern:
            folders = glob.glob(folder_pattern)
        else:
            folders = [folder_pattern]

        if not len(folders):
            print('No folders exist for {}'.format(folder_pattern))
            sys.exit(1)

        return folders

    def delete_folder_if_empty(self, folder):
        """Deletes a folder if it's empty.

        Args:
            folder: str, the fully qualified folder path.
        """
        num_of_files = len(os.listdir(folder))
        if num_of_files == 0:
            print("Deleting {} becaust it's empty".format(folder))
            if not self._dry_run:
                os.rmdir(folder)
            return True

        return False
