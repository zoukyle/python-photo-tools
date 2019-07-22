#!/bin/python

import file_utils


class ProcessorBase(object):

    def run(self, folder):
        pass


def main(arg_folder, processor):
    folders = file_utils.FileUtils().get_folders(arg_folder)
    for folder in folders:
        processor.run(folder)
