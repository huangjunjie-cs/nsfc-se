#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@author: huangjunjie
@file: pdf2imgs.py
@time: 2024/11/29
@desc: Make galleries images
"""

import os

from pdf2image import convert_from_path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BUILD_DIR = os.path.join(BASE_DIR, "..", "build")

PDF_DIR = os.path.join(BUILD_DIR, "examples")

# 读取PDF文件
for example_fname in os.listdir(PDF_DIR):
    if example_fname.endswith("pdf"):
        example_path = os.path.join(PDF_DIR, example_fname)
        images = convert_from_path(example_path)
        for i in range(len(images)):
            save_path = os.path.join(BUILD_DIR, "galleries", f"{example_fname}-{i}.jpg")
            images[i].save(save_path, "JPEG")
