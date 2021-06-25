# SlipBox

A hyperlink based format agnostic expert system (plain text).

## Features

### Formats

- [x] Markdown (SimpleMDE default)
- [ ] [GFM](https://github.github.com/gfm)
- [x] Zim Wiki (translated to Markdown)

### Pages

- [x] open Linked page
- [ ] Create
- [ ] Edit
- [ ] Save
- [ ] Delete
- [ ] File attachments
- [ ] Template support

### Management

- [x] open Random page
- [ ] Page Tree Browser
- [ ] Hyperlink assistant
- [ ] open Similar page
- [ ] Deduplication
- [ ] Search tools

### Visualization

- [ ] side-by-side view in a single tab
- [ ] interaktive Hyperlink web visualization
- [ ] interaktive Similarity web visualization (Sankey?)
- [ ] Minimap

### Sharing

* [ ] Twitter import
* [ ] Mastodon import
* [ ] Optical Character Recognition (for scans)
* [ ] Twitter export
* [ ] Print support
* [ ] full Twitter live sync

### Versioning

- [ ] Git support
- [ ] GitHup upload

### Security

- [ ] User Authentication
- [ ] Backups
- [ ] Backup encryption

### Marketing

- [ ] App icon, favicon.ico
- [ ] Screen shots for Github

## Install

Clone the Github repository:
```bash
git clone --recurse-submodules "https://github.com/pschwede/SlipBox"
cd SlipBox
```

Optional but recommended: Create and activate [a virtual environment for Python3](https://docs.python.org/3/library/venv.html).
Adapt `config.py` to your preferences using a text editor.
Install requirements.
```bash
pip install -r requirements.md
```

Run flask.
```bash
./run-flask.sh
```

Alternatively deploy this flask application using one of their [deployment options](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html).

## Usage

Open [the running instance](http://127.0.0.1:5000) in a web browser.

## Configuration

Edit `config.py`.
