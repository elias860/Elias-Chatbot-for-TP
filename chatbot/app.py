from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# The function
def get_bot_response(user_input):
    user_input = user_input.strip().lower() 
    
    if user_input == "what is ai?":
        return "AI stands for Artificial Intelligence, which is the simulation of human intelligence by machines."
    elif user_input == "how are you?":
        return "I'm just a program, but I'm doing great! How can I assist you?"
    elif user_input == "tell me a joke":
        return "Why did the computer show up at work late? It had a hard drive!"
    elif user_input == "who am i?":
        return "You are Mohamed Elyass Mohamed Ahmed, who always eager to learn new things, you are also trying your best to be selected in TP, am I true?"
    elif user_input == "yes you are true":
        return "Thank you, and wish you the best with your application, you will do it, you have high probability to be selected in TP"
    else:
        return "Sorry, I don’t understand that."

# main page route
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint for chatbot interaction
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True) 