from app import app


@app.route("/pcat/add")
def add_pcat():
    return "this is product category add operation"