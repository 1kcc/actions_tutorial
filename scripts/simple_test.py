#!/usr/bin/env python

import os
import numpy as np


def create_image(h, w, c=3):
    return np.random.randn(h, w, c)

def main():
    im = create_image(1028, 720, 3)
    print(im.shape)

if __name__ == '__main__':
    main()
