# -*- encoding: utf-8 -*-
from manim_imports_ext import *

import os
import subprocess


if __name__ == "__main__":
    dir = "videos"
    os.chdir(dir)

    str = ["SegmentTreeDiffScene", "SegmentTreeBuild"]
    bg = "../acm-clan/audio/bg2.mp3"

    file_content = "\n".join([k+".mp4" for k in str])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'tmp.mp4'])

    print("merge ok.")

