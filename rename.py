"""A command line tool to purge raw images which are missing corresponding JPGs.
"""
import getopt
import glob
import os
import sys

def Usage():
  help_doc = ('Usage example:\n'
              '  purge_raw.py -f 2013-12-30')
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

  jpg_files = glob.glob('%s/*.JPG' % folder)
  if not os.path.exists(folder):
    print('Folder %s does not exist.' % folder)
    sys.exit(1)

  for jpg_file in jpg_files:
    new_name = jpg_file.replace('641B', 'IMG_')
    print('rename %s to %s' % (jpg_file, new_name))
    os.rename(jpg_file, new_name)


if __name__ == '__main__':
  main()
  CalCERTS
