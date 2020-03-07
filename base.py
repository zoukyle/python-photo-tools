#!/bin/python

import file_utils


class ProcessorBase(object):

    def __init__(self, args):
        self._args = args
        self._file_utils = file_utils.FileUtils(dry_run=self._args.dry_run)

    def run(self, folder):
        pass


def main(arg_folder, processor):
    folders = file_utils.FileUtils().get_folders(arg_folder)
    for folder in folders:
        processor.run(folder)
