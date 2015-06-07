import re
p = re.compile(r'imgs_b\/(.*?)\.JPG')
a = """<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641C0129.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641C0129.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B5635.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B5635.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B5643.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B5643.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B5662.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B5662.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B5665.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B5665.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641A8176.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641A8176.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641A8196.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641A8196.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641A8273.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641A8273.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641A9961.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641A9961.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B1342.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B1342.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B1369.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B1369.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B1895.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B1895.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B2017.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B2017.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B2155.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B2155.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B2197.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B2197.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B5055.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B5055.jpg" alt="" /></a>
<a class="fancybox-thumb" href="{{ google_drive_dir }}/iframes/imgs_b/641B5075.JPG" rel="fancybox-thumb" title=""><img src="{{ google_drive_dir }}/iframes/imgs_s/641B5075.jpg" alt="" /></a>"""
b = p.findall(a)
counter = 0
output = '{% from "macros.j2" import render_image with context %}\n{% for image in ['
for i in b:
  counter = counter + 1
  if (counter % 4 == 0):
    output += "'%s',\n" % i
  else:
    output += "'%s', " % i
output += '] %}\n  {{ render_image(image) }}\n{% endfor %}'
print(output)
