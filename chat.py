from flask import Flask, request, jsonify
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("prompt")
    response = chat_with_gpt(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
