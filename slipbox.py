#!/usr/bin/env python3

"""
SlipBox server
Copyright (c) Peter Schwede
"""

import os
from datetime import datetime
from random import choice
from flask import Flask, render_template, escape, redirect, request
from glob import glob

from zim2md import zim2md
import config

app = Flask(__name__)


@app.route('/')
def index():
    """Default page"""
    return redirect(config.DEFAULT_PAGE, 301)


@app.route('/r')
@app.route('/rand')
@app.route('/random')
def random():
    """Picks a random page"""
    url = choice(glob(os.path.join(config.NOTES_HOME, "**.txt"),
        recursive=True) + glob(os.path.join(config.NOTES_HOME, "**.md")))
    return redirect(os.path.relpath(url, start=config.NOTES_HOME),
        307)


@app.route("/write/<path:path>", methods=['POST'])
def write(path):
    """Writes content to disk."""
    if request.method == "POST":
        with open(os.path.join(config.NOTES_HOME, path), "w") as _f:
            _f.write(request.get_data(as_text=True))
    return "1"


@app.route('/tree/<path:path>')
def tree(path):
    return render_template(
            "tree.html",
            plist=glob(os.path.join(path, '**.txt'))+glob(os.path.join(path, '**.md'))
            )


@app.route('/<path:path>')
@app.route('/pages/<path:path>')
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
        return render_template("editor.html", text=text, path=os.path.relpath(path, config.NOTES_HOME))
    except FileNotFoundError as _e:
        return render_template("editor.html", text="# %s\nCreated %s\n\n" % (
            path.split("/")[-1],
            datetime.now()),
            path=os.path.relpath(path, config.NOTES_HOME))

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
