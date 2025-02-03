from flask import Flask, request


app = Flask(__name__)

error_response = {"status": 500, "Message": "Something went wrong"}
resp_handler = lambda response: Flask.jsonify(response)


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World"


@app.route("/product/<int:id>", methods=["GET", "POST"])
def product_resource():
    # Check HTTP Method
    if request.method == "GET":
        try:
            id = request.queryParams["id"]
            response = get_products_by_id(id)
            return resp_handler(response)
        except Exception as e:
            return resp_handler(response)
    if request.method == "POST":
        try:
            payload = request.data
            response = add_new_product(payload)
            return resp_handler(response)
        except Exception as e:
            return resp_handler(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
