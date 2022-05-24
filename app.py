from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


""" Site general content """
TITLE, HEADING, CONTENT = "Page", "Welcome!", "This is a content generation schema"

""" Metas """
KEYWORDS, FAVICON, DESCRIPTION = "rat", "https://cdn.theflyingrat.com/favicon-16x16.png", "Just a page"

""" Assets to be loaded :D """
SCRIPTS = ["js.js", "another.js", "bla.js"]
STYLES = ["this", "that", "theother"]
PRELOAD = [["a", "style"], ["b", "script"]]


DATA = {
    "title": TITLE,
    "desc": DESCRIPTION,
    "heading": HEADING,
    "content": CONTENT,
    "styles": STYLES,
    "scripts": SCRIPTS,
    "keywords": KEYWORDS,
    "favicon": FAVICON,
    "preload": PRELOAD,
}


@app.route('/')
def index():
  return render_template('index.html', data=DATA)