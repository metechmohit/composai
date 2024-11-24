from flask import Blueprint, render_template, request, jsonify
from app.ai_generator import AIContentGenerator
from app.utils import format_content

main = Blueprint('main', __name__)
ai_generator = AIContentGenerator()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate_content():
    try:
        data = request.json
        topic = data.get('topic')
        keywords = data.get('keywords')
        tone = data.get('tone')
        length = data.get('length')

        # Generate content
        content = ai_generator.generate(topic, keywords, tone, length)
        formatted_content = format_content(content)

        return jsonify({
            'status': 'success',
            'content': formatted_content
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500