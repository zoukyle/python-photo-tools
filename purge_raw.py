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

  cr2_files = glob.glob('%s/*.CR2' % folder)
  delete_files = []
  for cr2_file in cr2_files:
    filename_base = cr2_file.split('.CR2')[0]
    if ('%s.JPG' % filename_base in jpg_files or
        '%s.jpg' % filename_base in jpg_files):
      continue
    delete_files.append(cr2_file)
  if not delete_files:
    print('No RAW file was deleted')
    sys.exit(0)

  user_input = input('The following RAW files will be deleted:\n%s\ny/N?'
                     % '\n'.join(delete_files))
  if user_input == 'y':
    for delete_file in delete_files:
      print('%s deleted' % delete_file)
      os.remove(delete_file)
  else:
    print('No RAW file was deleted')


if __name__ == '__main__':
  main()
