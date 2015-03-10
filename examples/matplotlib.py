#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import gl, library
from glumpy.api import matplotlib
from glumpy.transforms import *
from glumpy.graphics.collections import *

figure = matplotlib.Figure((24,12))
left  = figure.add_axes([0.010, 0.01, 0.485, 0.98],
                        facecolor=(1,0,0,0.25), aspect=1)
right = figure.add_axes([0.505, 0.01, 0.485, 0.98],
                        facecolor=(0,0,1,0.25), aspect=1)

trackball = Trackball(Position(), aspect=1.0)
collection = PointCollection("agg", transform=trackball, viewport=left.viewport)
left.attach(trackball)

panzoom = PanZoom(OrthographicProjection(Position(), normalize=True))
view = collection.view(transform=panzoom, viewport=right.viewport)
right.attach(panzoom)

collection.append(np.random.normal(0,.5,(15000,3)))

@left.event
def on_draw(dt):
    collection.draw()

@right.event
def on_draw(dt):
    view.draw(gl.GL_POINTS)

figure.show()
