#!/usr/bin/python

"""A command line tool to move video files from the Pictures folder to the
Videos folder.
"""
import datetime
import getopt
import os
import sys

def Usage():
  help_doc = ('Usage example:\n'
              '  move_videos.py -f folder-name')
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

  files = os.listdir(folder)

  for eachfile in files:
    if not eachfile.lower().endswith('mov'):
      continue

    # Ensures the folder exists in ~/Videos
    expected_dir = os.path.join('/cygdrive/c/Users/liangzou/Videos', folder)
    if not os.path.exists(expected_dir):
      os.mkdir(expected_dir)

    new_file_path = os.path.join(expected_dir, eachfile)
    print('moving %s to %s' % (eachfile, new_file_path))
    os.rename(os.path.join(folder, eachfile), new_file_path)


if __name__ == '__main__':
  main()
