# SlipBox

A hyperlink based format agnostic expert system (plain text).

## Features

### Formats

- [x] [Github Flavored Markdown](https://github.github.com/gfm) ([SimpleMDE](https://github.com/sparksuite/simplemde-markdown-editor) default)
- [x] [Zim Desktop Wiki](https://zim-wiki.org) (translated to GFM)

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

### Pages

- [x] Open
- [x] Edit
- [x] Create
- [x] Save
- [ ] Delete
- [ ] Subpages (Folders)
- [ ] File attachments
- [ ] Template support

### Versioning

- [ ] Git support
- [ ] Github upload

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


Add a `config.py`, for example:

```python
NOTES_HOME = "/your/path/to/your/notes"
DEFAULT_PAGE = "Home.txt"
DEFAULT_ENDING=".md"
DEBUG=True
HOST='0.0.0.0'
PORT='5000'
```

Run the server.
```bash
./slipbox.py
```

Alternatively deploy this flask application using one of their [deployment options](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html).

## Usage

Open [the running instance](http://127.0.0.1:5000) in a web browser.


Redirect `config.py` to your file. 

```bash
rm config.py && ln -s myconfig.py config.py
```
