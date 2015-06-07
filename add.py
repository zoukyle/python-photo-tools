import os
f = []
for (_, _, filenames) in os.walk('.'):
  f.extend(filenames)
  break
prefix = '641C'
for i in f:
  if '.JPG' not in i or prefix not in i:
    continue
  try:
    n = int(i.split('.')[0].replace(prefix, '').replace('-Edit', ''))
  except ValueError:
    continue
  if n < 163 or n > 424:
    continue
  print('<div style="display: block; text-align: center; margin-right: auto; margin-left: auto;">'
        '<img border="0" src="{{ google_drive_dir }}/%s" '
        'style="display: block; margin-right: auto; margin-left: auto; text-align: center;"></div>' % i)
  print('<br />')
