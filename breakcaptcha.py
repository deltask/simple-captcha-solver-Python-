#!/usr/bin/python

# [PoC] tesseract OCR script - tuned for scr.im captcha
#
# Chris John Riley
# blog.c22.cc
# contact [AT] c22 [DOT] cc
# 12/10/2010
# Version: 1.0
#
# Changelog
# 0.1> Initial version taken from Andreas Riancho's \
#      example script (bonsai-sec.com)
# 1.0> Altered to use Python-tesseract, tuned image \
#      manipulation for scr.im specific captchas
#

from PIL import Image
from tesseract import *
from tesseract import *

img = Image.open('captcha.png')
img = img.convert("RGBA")

pixdata = img.load()

# Make the letters bolder for easier recognition

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
     if pixdata[x, y][0] < 90:
         pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
     if pixdata[x, y][1] < 136:
         pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
     if pixdata[x, y][2] > 0:
         pixdata[x, y] = (255, 255, 255, 255)

img.save("input-black.gif")

#   Make the image bigger (needed for OCR)
original=Image.open('input-black.gif')
im_orig = original.resize((1000, 500), Image.NEAREST)

ext = ".tif"
im_orig.save("input-NEAREST"+ext)

#   Perform OCR using tesseract-ocr library
#from tesseract import image_to_string
image = Image.open('input-NEAREST.tif')
#rint image_to_string(image)')
print(image_to_string(image))
