#!/usr/bin/python
"""Library class for file utils."""

import glob
import sys


class FileUtils(object):
    """FileUtils class to manage files and folders."""

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
