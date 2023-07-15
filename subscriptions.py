from flask import Flask, request, jsonify
import seerbit

app = Flask(__name__)

publicKey = "SBPUBK_DQ24K6T5TI1WOAOYPWWYMGMHKDRVEGPW"

@app.route("/create-subscription", methods=["POST"])
def create_subscription():
    subscription_data = request.get_json()

    customer = seerbit.Customer(
        email=subscription_data["email"],
        cardNumber=subscription_data["cardNumber"],
        expiryMonth=subscription_data["expiryMonth"],
        expiryYear=subscription_data["expiryYear"],
        cvv=subscription_data["cvv"],
    )

    subscription = seerbit.Subscription(
        publicKey=publicKey,
        customer=customer,
        amount=subscription_data["amount"],
        currency="NGN",
        productDescription="My subscription",
    )

    response = subscription.create()

    if response.status == "SUCCESS":
        return jsonify({"status": "SUCCESS"})
    else:
        return jsonify({"status": "ERROR", "message": response.message})

if __name__ == "__main__":
    app.run()
