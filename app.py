from flask import Flask, request, jsonify

app = Flask(__name__)

# Conversion rate (example: 1 USD = 83 INR)
USD_TO_INR_RATE = 83

@app.route('/convert', methods=['GET'])
def convert_usd_to_inr():
    try:
        usd_amount = float(request.args.get('usd'))
        inr_amount = usd_amount * USD_TO_INR_RATE
        return jsonify({
            "usd": usd_amount,
            "inr": inr_amount
        })
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide a valid USD amount."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
