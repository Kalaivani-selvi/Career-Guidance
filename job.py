

# # openai.api_key = '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'

# import openai
# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# # Replace 'your_openai_api_key_here' with your actual OpenAI API key
# openai.api_key = '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'

# def get_openai_response(message):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": message}]
#         )
#         return response.choices[0].message['content'].strip()
#     except Exception as e:
#         print(f"Error: {e}")
#         return "I'm sorry, I couldn't process that request."

# @app.route('/')
# def openai():
#     return render_template('openai.html')

# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     data = request.json
#     user_message = data.get('message')
    
#     if not user_message:
#         return jsonify({'error': 'No message provided'}), 400

#     response = get_openai_response(user_message)
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chatbot')
def openai():
    return render_template('openai.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = get_chatbot_response(user_message)
    return jsonify({"message": response["result"]})

def get_chatbot_response(user_message):
    url = "https://open-ai21.p.rapidapi.com/conversationgpt35"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "web_access": False,
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "5167fad87bmshd240cb454662cebp106d20jsne4de16f885fd",
        "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)


