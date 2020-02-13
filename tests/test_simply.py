#!/usr/bin/env python

from simple_test import create_image

def test_create_image():
    shape = (100, 100, 3)
    im = create_image(*shape)
    assert im.shape == shape, 'Shape did not match'
