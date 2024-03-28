import staintools
import imageio
import os, shutil
import glob
import numpy as np
import cv2
import pickle
import argparse
import time

start=time.time()

parser = argparse.ArgumentParser()
parser.add_argument('--slide_id', help='Slide id', type=str, required=True)
parser.add_argument('--output_id',help='Output path', type=str, required=True)
args = parser.parse_args()

STANDARDIZE_BRIGHTNESS = True
METHOD = "macenko"
target = "/BiO/jolee/tools/corNormalization/Ref.png"

normalizer = staintools.StainNormalizer(method=METHOD)
target = staintools.read_image(target)
target = staintools.LuminosityStandardizer.standardize(target)
normalizer.fit(target)

input = args.slide_id
output = args.output_id



img = staintools.read_image(input)
img = staintools.LuminosityStandardizer.standardize(img)
img_normalized = normalizer.transform(img)
imageio.imwrite(output, img_normalized)

end = time.time()-start
print(end)


