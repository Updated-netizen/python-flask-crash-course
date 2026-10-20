from flask import Flask
app = Flask(__name__)

#URL paramerter
@app.route("/users/<username>")
def get_username(username):
    return f"hello{username}"

#Query parameters
@app.route(intell"/products/", method=["GET"])
def get_product():
     name = request.args.get("name")


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/products", method=["POST"])
def create_product():
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        return {
            "name":name,
            "email":email
        }
    