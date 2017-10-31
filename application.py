from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """Render Homepage of the app"""
    return "Home Page"


@app.route("/catalog/<string:category>/items")
def items(category):
    """Render list of items per category"""
    return "items of category %s" % category


@app.route("/catalog/<string:category>/<string:item>")
def item(category, item):
    """Render a specific item"""
    return "show item %s of category %s" % (item, category)


@app.route("/catalog/<string:category>/<string:item>/edit")
def edit_item(category, item):
    """Render an edit form for a specific item"""
    return "edit item %s of category %s" % (item, category)


@app.route("/catalog/<string:category>/<string:item>/delete")
def delete_item(category, item):
    """Render an delete form for a specific item"""
    return "delete item %s of category %s" % (item, category)


@app.route("/catalog.json")
def api_catalog():
    """Return catalog json"""
    return "json content of catalog"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
