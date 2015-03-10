# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------
from glumpy import app, gloo, gl, transforms
from . axes import Axes

class Figure(object):
    """ """

    def __init__(self, figsize=(10,10), dpi=72, color=(.95,.95,.95,1)):
        width = int(round(figsize[0] * dpi))
        height = int(round(figsize[1] * dpi))
        self.window = app.Window(width=width, height=height, color=color,
                                 title = "Figure (matplotlib API)")
        self.viewport = app.Viewport()

    def on_draw(self, dt):
        self.window.clear()

    def show(self):
        self.window.push_handlers(self.viewport)
        self.window.push_handlers(self)
        app.run()

    def add_axes(self, rect, facecolor=(1,1,1,1), aspect=None):
        axes = Axes(rect, facecolor, aspect)
        self.viewport.add(axes)
        return axes
