import cv2  
import os
import shutil
import numpy as np
from argparse import ArgumentParser

RECTANGLE_RATIO_TO_IMG_SIZE = 0.1

def get_points_to_draw_rectangle_on_top(height, width):
     return (0, 0), (width, int(height * RECTANGLE_RATIO_TO_IMG_SIZE))

def get_points_to_draw_rectangle_on_center(height, width):
    rectangle_height = height
    rectangle_width = width * RECTANGLE_RATIO_TO_IMG_SIZE
    return (int(width / 2 - rectangle_width / 2),  int(height / 2 - rectangle_height / 2)), \
         (int(width / 2 + rectangle_width / 2), int(height / 2 + rectangle_height / 2))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("in_dir", type=str, help="input images directory")
    parser.add_argument("out_dir", type=str, help="output images directory")
    parser.add_argument("--rectangle_position", type=str, default="center", help="where the black rectangle will be drawn, options: top or center")
    args = parser.parse_args()

    if (args.rectangle_position == "top"):
        get_start_and_end_points = get_points_to_draw_rectangle_on_top
    else:
        get_start_and_end_points = get_points_to_draw_rectangle_on_center

    in_dir = args.in_dir
    out_dir = args.out_dir
    if in_dir[-1] != "/":
        in_dir = in_dir + "/"
    if out_dir[-1] != "/":
        out_dir = out_dir + "/"


    for filename in os.listdir(in_dir):    
        img = cv2.imread(in_dir + filename)

        shutil.copy2(in_dir + filename, out_dir) 

        height = img.shape[0]
        width = img.shape[1]
        start_point, end_point = get_start_and_end_points(height, width)
        color = (0, 0, 0) 
        thickness = -1
        img = cv2.rectangle(img, start_point, end_point, color, thickness) 
        

        cv2.imwrite(out_dir + filename, img)