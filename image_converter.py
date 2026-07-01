import argparse
import pathlib

import PIL.Image

parser = argparse.ArgumentParser(description='Converts images')
parser.add_argument('input', help='The image to convert')
parser.add_argument('-o', '--output', default="*.ico", help='Output FileName. Use * to capture input name.')
args = parser.parse_args()

input: str = args.input
output: str = args.output.replace("*", pathlib.Path(args.input).stem)

print(f"Converting `{input}` to `{output}`...")

img = PIL.Image.open(input)
img.save(output)

print(f"Success.")