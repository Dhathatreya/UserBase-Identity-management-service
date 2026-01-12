from app import app
from model.user_model import user_model
obj = user_model()
@app.route("/user/signup")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone")
def user_addone_controller():
    return obj.user_addone_model()
