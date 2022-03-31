from flask import Flask, render_template,jsonify,request
import string
import random
import base64

app = Flask(__name__ , template_folder='templates', static_folder='static')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/ui", methods=['GET','POST'])
def ui():
    if request.method == "POST":
        Immutable_Multi_Dict = request.form
        nick_name = dict(Immutable_Multi_Dict)['fname']
        z=nick_name.replace(" ","+").split(",")[1]
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        y = base64.b64decode(z)
        fi = open("./testfileupload/"+x+".jpg", "wb")
        fi.write(y)
        fi.close()
        return jsonify(({"valid":True}))
    else:
        return jsonify(({"valid":'Content-Type not supported!'}))


@app.route("/products")
def products():
    return "<p>This is products page</p>"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)