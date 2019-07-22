#!/usr/bin/python

import argparse

common_parser = argparse.ArgumentParser(add_help=False)
common_parser.add_argument('-f',
                           '--folder',
                           type=str,
                           help='The folder to process')
common_parser.add_argument('--dry_run',
                           dest='dry_run',
                           action='store_true',
                           help='Dry run without renaming')
common_parser.add_argument('--nodry_run', dest='dry_run', action='store_false')
