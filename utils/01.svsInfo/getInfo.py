import os
import openslide
import glob
import numpy as np
from pandas import DataFrame
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--prj', help='project name', type=str, required=True)
args = parser.parse_args()

prj = args.prj


slide_path = os.path.join( prj, "svs")
slide_list = glob.glob(os.path.join(slide_path, "*.svs"))

if not os.path.exists(os.path.join(slide_path, "Info")):
    os.makedirs(os.path.join(slide_path, "Info"))


for f in slide_list :
    svs = openslide.OpenSlide(f)
    print("--get svs file --")
    properties = svs.properties
    dt = pd.DataFrame(properties.items())
    fname = os.path.basename(f).replace('.svs','')
    dt['Name'] = fname
    dt.columns = ['Feature','Value','Name']
    dt.to_csv(os.path.join(slide_path, "Info", fname+".txt"), sep= "\t", index = False)

