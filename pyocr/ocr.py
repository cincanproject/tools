#!/usr/bin/env python3

import io
import os
from PIL import Image as PI
import pyocr
import pyocr.builders
import sys
from wand.image import Image

import argparse

def main(argv):
    tool = pyocr.get_available_tools()[0]

    argparser = argparse.ArgumentParser()
    argparser.add_argument('file', action='store', help='File to OCR (PNG, JPG, PDF)')
    argparser.add_argument('-l', dest='lang', default='eng', help='language to use')
    argparser.add_argument('-d', dest='digits', action='store_true', help='only OCR for digits')
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
        if args.digits:
            digits = tool.image_to_string(
                PI.open(io.BytesIO(img)),
                lang=args.lang,
                builder=pyocr.tesseract.DigitBuilder())
            final_text.append(digits)
        else:
            txt = tool.image_to_string(
                PI.open(io.BytesIO(img)),
                lang=args.lang,
                builder=pyocr.builders.TextBuilder())
            final_text.append(txt)

    print(''.join(final_text))

if __name__ == '__main__':
    main(sys.argv)

