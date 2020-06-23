#!/usr/bin/env python3

import io
import os
from PIL import Image as PI
import pyocr
import pyocr.builders
import sys
from wand.image import Image

import cv2

import argparse
import numpy as np

# Borrowed some code from here:
# https://stackoverflow.com/questions/48327567/removing-horizontal-underlines/48365071#48365071
# Tesseract does not handle underlined text very well. Links are sometimes underlined,
# so you can remove the underlining with this function.
def remove_underline(img):
    img = cv2.imdecode(np.frombuffer(img.read(), np.uint8), 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## (1) Create long line kernel, and do morph-close-op
    kernel = np.ones((1, 40), np.uint8)
    morphed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    ## (2) Invert the morphed image, and add to the source image:
    dst = cv2.add(gray, (255 - morphed))
    is_success, buf = cv2.imencode(".png", dst)
    if is_success:
        return io.BytesIO(buf)
    else:
        print("Failed to encode de-underlined image", file=sys.stderr)
        sys.exit(1)

def main(argv):
    tool = pyocr.get_available_tools()[0]

    argparser = argparse.ArgumentParser()
    argparser.add_argument('file', action='store', help='File to OCR (PNG, JPG, PDF)')
    argparser.add_argument('-l', dest='lang', default='eng', help='language to use')
    argparser.add_argument('-d', dest='digits', action='store_true', help='only OCR for digits')
    argparser.add_argument('-u', dest='underline', action='store_true', help='preprocess underlined text')
    args = argparser.parse_args()

    if args.lang not in tool.get_available_languages():
        print(f"ocr language '{args.lang}' not available", file=sys.stderr)
        os.exit(1)
    if len(sys.argv) <= 1:
        argparser.print_help(sys.stderr)
        os.exit(1)

    req_image = []
    final_text = []
    image_in = Image(filename=args.file)
    image_jpeg = image_in.convert('png')
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('png'))
    for img in req_image:
        img_buf = io.BytesIO(img)

        if args.underline:
            img_buf = remove_underline(img_buf)

        if args.digits:
            digits = tool.image_to_string(
                PI.open(img_buf),
                lang=args.lang,
                builder=pyocr.tesseract.DigitBuilder())
            final_text.append(digits)
        else:
            txt = tool.image_to_string(
                PI.open(img_buf),
                lang=args.lang,
                builder=pyocr.builders.TextBuilder())
            final_text.append(txt)

    print(''.join(final_text))

if __name__ == '__main__':
    main(sys.argv)

