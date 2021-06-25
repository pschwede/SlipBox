#!/usr/bin/env python

"""
SlipBox server
Copyright (c) Peter Schwede
"""

import os
from random import choice
from flask import Flask, render_template, escape, redirect
from glob import glob

from zim2md import zim2md
import config

app = Flask(__name__)


@app.route('/')
def index():
    """"""
    return redirect("Home.txt", 301)


@app.route('/r')
@app.route('/rand')
@app.route('/random')
def random():
    """Picks a random page"""
    url = choice(glob(os.path.join(config.NOTES_HOME, "**/*.txt"),
        recursive=True))
    return redirect(os.path.relpath(url, start=config.NOTES_HOME),
        307)


@app.route('/<path:path>')
def open_page(path):
    """Default access to pages."""
    try:
        path = os.path.join(config.NOTES_HOME, path)
        text = ""
        with open(path, "r") as _f:
            text = _f.readlines()
            if zim2md.compatible(path):
                text = zim2md.translate(text=text,
                        path=os.path.relpath(path,
                            start=config.NOTES_HOME))
        return render_template("editor.html", text=text)
    except FileNotFoundError as _e:
        return render_template("error.html", error=_e)
