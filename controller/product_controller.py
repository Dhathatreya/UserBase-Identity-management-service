from app import app


@app.route("/product/add")
def add_product():
    return "this is product add operation"