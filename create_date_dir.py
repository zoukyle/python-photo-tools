#!/usr/bin/python

"""A command line tool to create a directory with today's date.
"""
import datetime
import getopt
import os
import sys

def Usage():
  help_doc = ('Usage example:\n'
              '  create_date_dir.py -f Movies')
  print(help_doc)


def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help', 'folder='])
  except getopt.GetoptError as err:
    print(str(err))
    sys.exit(1)
  folder = ''
  for o, a in opts:
    if o in ('-h', '--help'):
      Usage()
      sys.exit(0)
    elif o in ('-f', '--folder'):
      folder = a
  if not folder:
    print('The folder must be set')
    sys.exit(1)

  nowtime = datetime.datetime.now()
  expected_dir = os.path.join(folder, nowtime.date().isoformat())
  if os.path.exists(expected_dir):
    return
  os.mkdir(expected_dir)


if __name__ == '__main__':
  main()
  
