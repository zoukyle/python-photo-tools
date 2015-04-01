#!/usr/bin/python

"""A command line tool to batch process MLV files.
"""
import getopt
import glob
import os
import sys
import subprocess

MLV_DUMP = '/Users/liangzou/mlv_rec/mlv_dump'

def Usage():
  help_doc = ('Usage example:\n'
              '  batch_mlv.py -f 2013-12-30')
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

  mlv_files = glob.glob('%s/*.MLV' % folder)
  if not os.path.exists(folder):
    print('Folder %s does not exist.' % folder)
    sys.exit(1)

  for mlv_file in mlv_files:
    # mlv_file, e.g. test/M29-1622.MLV, name will be M29-1622
    name = os.path.basename(mlv_file).split('.')[0]
    # subfolder, e.g. test/M29-1622
    subfolder = os.path.join(folder, name)
    if not os.path.exists(subfolder):
      os.mkdir(subfolder)
    output_mov = os.path.join(subfolder, '%s.mov' % name)
    if os.path.exists(output_mov):
      continue
    # Go ahead and run mlv_dump
    command = [MLV_DUMP, '--dng', '-o',
               os.path.join(subfolder, name + '.'), mlv_file]
    exit_code = subprocess.call(command)
    if (exit_code != 0):
      raise ValueError('Unexpected error when processing %s' % mlv_file)


if __name__ == '__main__':
  main()
  
