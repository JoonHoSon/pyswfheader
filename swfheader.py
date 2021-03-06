# coding:utf-8
__author__ = 'JoonHo Son'

import sys
import hexagonit.swfheader


def main(string):
    """
    hexagonit 모듈을 이용해서 대표적인 정보를 추출한다.
    """
    meta = hexagonit.swfheader.parse(string)
    list(sorted(meta.keys()))
    duration = meta['frames'] / meta['fps']

    print("width : %d" % meta['width'])
    print("height : %d" % meta['height'])
    print("frames : %d" % meta['frames'])
    print("fps : %d" % meta['fps'])
    print("duration : %d" % duration)


if __name__ == "__main__":
    main(sys.argv[1])