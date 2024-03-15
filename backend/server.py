from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__) 
genai_api_key = "AIzaSyC897bCsmDp-Yc9fCrZtuj_0Pux_YMop6o"

@app.route('/test', methods=['GET'])
def test():
    return "Hello, World!"

# @app.route('/<name>', methods=['GET'])
# def name(name):
#     return f"Hello, {name}!"

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']
    
    genai.configure(api_key=genai_api_key)

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,  
        "top_k": 5,     
        "max_output_tokens": 50,  
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    
    convo = model.start_chat(history=[
    ])

    prompt = "Sumarize the following complaint in very short just give me sumary only in plain text: " + text

    convo.send_message(prompt)
    summary = convo.last.text
    return jsonify({"summary": summary})


if __name__ == '__main__':
    app.run(debug=True, port=5000)



