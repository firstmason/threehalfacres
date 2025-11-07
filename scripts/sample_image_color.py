#!/usr/bin/env python3
from PIL import Image
from collections import Counter
import sys

path = '../three-half-aacres.jpg'
# If called with a path argument, use it
if len(sys.argv) > 1:
    path = sys.argv[1]

img = Image.open(path).convert('RGB')
w,h = img.size
# sample a centered box (20x20 or smaller if image small)
box_size = min(40, w//4, h//4)
left = max(0, w//2 - box_size//2)
upper = max(0, h//2 - box_size//2)
right = min(w, left + box_size)
lower = min(h, upper + box_size)
region = img.crop((left, upper, right, lower))
px = list(region.getdata())
# compute average
r = sum(p[0] for p in px) / len(px)
g = sum(p[1] for p in px) / len(px)
b = sum(p[2] for p in px) / len(px)
avg = (int(round(r)), int(round(g)), int(round(b)))
# find most common color in sampled region
most_common = Counter(px).most_common(1)[0][0]

hex_avg = '#%02x%02x%02x' % avg
hex_common = '#%02x%02x%02x' % most_common
print(hex_avg, hex_common)
