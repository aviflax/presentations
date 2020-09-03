#!/usr/bin/env python3

# Requires Pillow: $ pip3 install pillow

from PIL import Image, ImageFont, ImageDraw
import sys

font = ImageFont.truetype("Merriweather-Bold.ttf", 200)


def main(image_file_path, text):
  with Image.open(image_file_path) as img:
      draw = ImageDraw.Draw(img)
      text_width, text_height = draw.textsize(text, font)
      x = (img.width / 2) - (text_width / 2)
      y = img.height - text_height
      draw.text((x, y), text, fill=(0, 0, 0), font=font)
      img.save(image_file_path)

  return True

if __name__ == '__main__':
  image_file_path = sys.argv[1]
  text = sys.argv[2]
  main(image_file_path, text)
