#!/usr/bin/env python3

# Requires Pillow: $ pip3 install pillow

from PIL import Image, ImageFont, ImageDraw
import sys

font = ImageFont.truetype("Merriweather-Bold.ttf", 25)

def main(image_file_path, text):
  img = Image.open(image_file_path)
  ImageDraw.Draw(img).text((0,0), text, (255,255,0), font=font)
  img.save('overlay_' + image_file_path)
  return True

if __name__ == '__main__':
  image_file_path = sys.argv[1]
  text = sys.argv[2]
  main(image_file_path, text)
