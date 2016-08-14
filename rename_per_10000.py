import os
for i in range(37, 39):
  old = '641C%04d.JPG' % i
  old1 = '641C%04d.CR2' % i
  new = '641D%04d.JPG' % i
  new1 = '641D%04d.CR2' % i
  print('move %s to %s' % (old, new))
  os.rename(old, new)
  print('move %s to %s' % (old1, new1))
  os.rename(old1, new1)