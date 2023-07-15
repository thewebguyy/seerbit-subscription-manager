from flask import Flask, jsonify
import seerbit

app = Flask(__name__)

publicKey = "your_public_key"

# Create a subscription
@app.route("/create-subscription", methods=["POST"])
def create_subscription():
    customer = seerbit.Customer(
        email="customer@example.com",
        cardNumber="4111111111111111",
        expiryMonth="12",
        expiryYear="2023",
        cvv="123",
    )

    subscription = seerbit.Subscription(
        publicKey=publicKey,
        customer=customer,
        amount="2000",
        currency="NGN",
        productDescription="My subscription",
    )

    response = subscription.create()

    if response.status == "SUCCESS":
        return jsonify({"status": "SUCCESS"})
    else:
        return jsonify({"status": "ERROR", "message": response.message})

# Charge a subscription
@app.route("/charge-subscription", methods=["POST"])
def charge_subscription():
    billingId = "your_billing_id"

    response = seerbit.charge(publicKey=publicKey, billingId=billingId)

    if response.status == "SUCCESS":
        return jsonify({"status": "SUCCESS"})
    else:
        return jsonify({"status": "ERROR", "message": response.message})

# Get customer subscriptions
@app.route("/get-customer-subscriptions", methods=["GET"])
def get_customer_subscriptions():
    response = seerbit.get_subscriptions(publicKey=publicKey)

    if response.status == "SUCCESS":
        return jsonify(response.data)
    else:
        return jsonify({"status": "ERROR", "message": response.message})

# Update customer subscriptions
@app.route("/update-customer-subscriptions", methods=["PUT"])
def update_customer_subscriptions():
    billingId = "your_billing_id"
    amount = "2000"

    response = seerbit.update_subscriptions(
        publicKey=publicKey, billingId=billingId, amount=amount
    )

    if response.status == "SUCCESS":
        return jsonify({"status": "SUCCESS"})
    else:
        return jsonify({"status": "ERROR", "message": response.message})

# Validate OTP
@app.route("/validate-otp", methods=["POST"])
def validate_otp():
    otp = "your_otp"

    response = seerbit.validate_otp(publicKey=publicKey, otp=otp)

    if response.status == "SUCCESS":
        return jsonify({"status": "SUCCESS"})
    else:
        return jsonify({"status": "ERROR", "message": response.message})

# Get merchant subscriptions
@app.route("/get-merchant-subscriptions", methods=["GET"])
def get_merchant_subscriptions():
    response = seerbit.get_merchant_subscriptions(publicKey=publicKey)

    if response.status == "SUCCESS":
        return jsonify(response.data)
    else:
        return jsonify({"status": "ERROR", "message": response.message})

if __name__ == "__main__":
    app.run()
