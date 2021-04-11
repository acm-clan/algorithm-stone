# -*- encoding: utf-8 -*-
from manim_imports_ext import *

import os
import subprocess


if __name__ == "__main__":
    dir = "videos"

    videos = ["SegmentTreeDiffScene", "SegmentTreeWhatIs", "SegmentTreeBuild", "SegmentTreeUpdate", "SegmentTreeQuery"]
    bg = "E:/Sources/acm-clan/audio/bg003.mp3"

    # for k in videos:
    #     subprocess.call(['python3', '-m', 'manimlib', 'segmenttree.py', k, '-w'])

    os.chdir(dir)
    file_content = "\n".join(["file '"+k+".mp4'" for k in videos])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-y', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'segment.mp4'])
    subprocess.call(['ffmpeg', '-y', '-i', 'segment.mp4', '-stream_loop', '-1', '-i', bg, '-shortest', '-c:v', 'copy', '-c:a', 'aac', 'output.mp4'])

    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4

    print("merge ok.")

