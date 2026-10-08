from flask import Flask, request, jsonify
import pickle

# AI Model load karna
with open("mera_ai_model.pkl", "rb") as f:
    vectorizer, ai_brain = pickle.load(f)

app = Flask(__name__)

# Server check karne ke liye base link
@app.route("/")
def home():
    return "Tera Scam Detector API Live Hai!"

# Tera main scanning engine
@app.route("/scan", methods=["GET"])
def scan_message():
    msg = request.args.get("msg")
    if not msg:
        return jsonify({"error": "Message bhej check karne ke liye!"})
    
    msg_numbers = vectorizer.transform([msg])
    prediction = ai_brain.predict(msg_numbers)
    result = "SCAM" if prediction[0] == 1 else "SAFE"
    
    return jsonify({
        "tera_message": msg,
        "ai_result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
