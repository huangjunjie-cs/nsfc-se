#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: huangjunjie-cs
@file: make_demo.py
@time: 2024/12/08
"""

import os
import logging
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("--dirpath", default=BASE_DIR, help="当前目录")
parser.add_argument("--src_fpath", default="青年正文2024.tex", help="src_fpath")
parser.add_argument("--dst_fpath", default="青年正文2024-se.tex", help="dst_fpath")
args = parser.parse_args()

# https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

logger = logging.getLogger(__file__)
logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def replace_file(
    src_fpath="青年正文2024.tex",
    dst_fpath="青年正文2024-se.tex",
    pattern=r"\usepackage[windows]{nsfc}",
    replace_pattern=r"\usepackage[windows]{nsfc_se}",
):
    """
    This function will replace pattern in src_fpath and output into dst_fpath
    """
    output_f = open(dst_fpath, "w")
    cnt = 0
    with open(src_fpath) as f:
        for line in f:
            if line.find(pattern) > -1:
                output = line.replace(pattern, replace_pattern)
                cnt += 1
            else:
                output = line
            print(output, file=output_f)
    output_f.close()
    logger.info(f"{src_fpath} replace {cnt} times, and output {dst_fpath}")


def main():
    src_fpath = args.src_fpath
    dst_fpath = args.dst_fpath
    replace_file(src_fpath=src_fpath, dst_fpath=dst_fpath)


if __name__ == "__main__":
    main()
