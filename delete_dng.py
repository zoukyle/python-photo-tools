#!/usr/bin/python

"""A command line tool to delete DNG files if the MOV file has been generated.
"""
import getopt
import glob
import os
import sys
import subprocess

def Usage():
  help_doc = ('Usage example:\n'
              '  delete_png.py -f 2013-12-30')
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
    # mlv_file, e.g. test/M29-1622.MLV, folder is test, name will be M29-1622
    name = os.path.basename(mlv_file).split('.')[0]
    # subfolder, e.g. test/M29-1622
    subfolder = os.path.join(folder, name)
    if not os.path.exists(subfolder):
      continue
    output_mov = os.path.join(subfolder, '%s.mov' % name)
    if not os.path.exists(output_mov):
      continue
    # Go ahead and delete the DNG files
    delete_files = glob.glob('%s/*.dng' % subfolder)
    delete_files.extend(glob.glob('%s/*.wav' % subfolder))
    if not delete_files:
      print('No DNG to delete in ' + subfolder)
      continue
    user_input = raw_input('The following DNG files will be deleted:\n%s\n?' % '\n'.join(delete_files))
    if user_input == 'y':
      for delete_file in delete_files:
        print('%s deleted' % delete_file)
        os.remove(delete_file)
    else:
      print('No DNG file was deleted')


if __name__ == '__main__':
  main()
  
