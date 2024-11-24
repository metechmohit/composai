from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import groq
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Groq client
client = groq.Groq(
    api_key=os.getenv('GROQ_API_KEY')
)

@app.route('/')
def serve_app():
    with open('compos.html', 'r', encoding='utf-8') as file:
        return file.read()

@app.route('/api/generate', methods=['POST'])
def generate_content():
    try:
        data = request.json
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'No topic provided'}), 400

        # Construct the prompt for the article
        prompt = f"""Write a comprehensive, engaging, and well-structured article about {topic}.
        The article should:
        - Have a compelling introduction
        - Include relevant information and facts
        - Be organized into clear sections
        - Have a natural flow
        - End with a strong conclusion
        Please write in a professional yet engaging tone and aim for around 500 words."""

        # Make the API call to Groq
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Using Mixtral model for better quality
            messages=[
                {"role": "system", "content": "You are a professional content writer skilled at creating engaging and informative articles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500,
            top_p=1,
            stream=False
        )

        # Extract the generated content
        generated_content = completion.choices[0].message.content

        return jsonify({
            'success': True,
            'content': generated_content
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)