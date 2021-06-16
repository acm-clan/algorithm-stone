# -*- encoding: utf-8 -*-
from manim_imports_ext import *

import os
import subprocess

def merge_segmenttree():
    dir = "videos"

    videos = ["SegmentTreeDiffScene", "SegmentTreeWhatIs", "SegmentTreeBuild", "SegmentTreeUpdate", "SegmentTreeQuery"]
    bg = "E:/Sources/acm-clan/audio/bg003.mp3"

    for k in videos:
        subprocess.call(['python3', '-m', 'manimlib', 'segmenttree.py', k, '-w'])

    os.chdir(dir)
    file_content = "\n".join(["file '"+k+".mp4'" for k in videos])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-y', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'output.mp4'])
    subprocess.call(['ffmpeg', '-y', '-i', 'output.mp4', '-stream_loop', '-1', '-i', bg, '-shortest', '-c:v', 'copy', '-c:a', 'aac', 'segment.mp4'])

    os.remove("output.mp4")
    os.remove("filelist.txt")

    print("merge ok.")

def merge_rbtree():
    dir = "videos"

    videos = ["RedBlackTreeWhatIs", "RedBlackTreeRotate", "RedBlackTreeInsert", "RedBlackTreeDelete", "RedBlackTreeEnd"]
    bg = "E:/Sources/acm-clan/audio/bg004.mp3"

    for k in videos:
        subprocess.call(['python3', '-m', 'manimlib', 'rb.py', k, '-w'])

    os.chdir(dir)
    file_content = "\n".join(["file '"+k+".mp4'" for k in videos])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-y', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'output.mp4'])
    subprocess.call(['ffmpeg', '-y', '-i', 'output.mp4', '-stream_loop', '-1', '-i', bg, '-shortest', '-c:v', 'copy', '-c:a', 'aac', 'rbtree.mp4'])

    os.remove("output.mp4")
    os.remove("filelist.txt")

    print("merge ok.")

def merge_kmp():
    dir = "videos"

    videos = ["KmpPrefixScene", "KmpScene"]
    bg = "E:/Sources/acm-clan/audio/bg002.mp3"

    for k in videos:
        subprocess.call(['python3', '-m', 'manimlib', 'kmp.py', k, '-w'])

    os.chdir(dir)
    file_content = "\n".join(["file '"+k+".mp4'" for k in videos])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-y', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'output.mp4'])
    subprocess.call(['ffmpeg', '-y', '-i', 'output.mp4', '-stream_loop', '-1', '-i', bg, '-shortest', '-c:v', 'copy', '-c:a', 'aac', 'kmp.mp4'])

    os.remove("output.mp4")
    os.remove("filelist.txt")

    print("merge ok.")

def merge_trie():
    dir = "videos"

    videos = ["TrieScene"]
    bg = "E:/Sources/acm-clan/audio/a_new_chapter.mp3"

    for k in videos:
        subprocess.call(['python3', '-m', 'manimlib', 'trie.py', k, '-w'])

    os.chdir(dir)
    file_content = "\n".join(["file '"+k+".mp4'" for k in videos])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-y', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'output.mp4'])
    subprocess.call(['ffmpeg', '-y', '-i', 'output.mp4', '-stream_loop', '-1', '-i', bg, '-shortest', '-c:v', 'copy', '-c:a', 'aac', 'trie.mp4'])

    os.remove("output.mp4")
    os.remove("filelist.txt")

    print("merge ok.")

if __name__ == "__main__":
    merge_trie()

