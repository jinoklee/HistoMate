import os
import glob
import cv2
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def get_parser():
    parser = argparse.ArgumnetParser(descriptioin="pathQC")
    parser.add_argument("-d","--path_dir", type=str,required=True)
    return parser

def process(args):
    img_list=glob.glob("%s/*img"%args.path_dir)

    size_px= 512
    edge_value = []

    for f in flist:
        img = cv2.imread(f)
        ed = cv2.Canny(img, 40, 100)
        ed = ed / np.max(ed)
        ed = (np.sum(np.sum(ed)) / (size_px * size_px)) * 100
        edge_value.append(ed)

    df=pd.DataFrame({'file':img_list, 'edge': edge_value})
    df.to_csv("patchlist_addedge.txt", sep="\t",index = False)



    ## Color SD
    sd = []

    for img in img_list: 
        image = cv2.imread(img) 
        image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
        image = np.std(image)
        sd.append(image)

    df['rgb_sd']=sd


    ## stat
    n, bins, patches = plt.hist(df['edge'], bins=100)
    plt.vlines(x=25, ymin=0, ymax=2000, color='red', linestyle='dotted')
    plt.savefig('edge.png', dpi=300)

    n, bins, patches = plt.hist(df['rgb_sd'], bins=100)
    plt.savefig('sd.png', dpi=300)

    ## show 
    for re in result:
    images = []
    for img_path in re:
        rgb = cv2.imread(img_path, cv2.IMREAD_COLOR) 
        images.append(cv2.cvtColor(rgb,cv2.COLOR_BGR2RGB))


    plt.figure(figsize=(10,10))
    columns = 10

    for i, img in enumerate(images):
        plt.subplot(int(len(images) / columns + 1), columns, i + 1)
        plt.gca().axes.xaxis.set_visible(False)
        plt.gca().axes.yaxis.set_visible(False)
        plt.imshow(img)
        plt.savefig('img_{}'.format(i))
