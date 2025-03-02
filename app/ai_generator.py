import groq
from config import Config

class AIContentGenerator:
    def __init__(self):
        self.client = groq.Client(api_key=Config.GROQ_API_KEY)

    def create_prompt(self, topic, keywords, tone, length):
        prompt = f"""
        Write a {tone.lower()} article about "{topic}".
        Keywords to include: {keywords}
        Length: approximately {length} words

        Requirements:
        - Use a {tone.lower()} tone throughout
        - Include an engaging introduction
        - Break content into relevant sections with subheadings
        - Naturally incorporate the keywords: {keywords}
        - Conclude with a strong summary
        - Make it informative and engaging
        - Ensure content is original and well-structured

        Format the output in markdown.
        """
        return prompt

    def generate(self, topic, keywords, tone, length):
        prompt = self.create_prompt(topic, keywords, tone, length)
        
        try:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a professional content writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")
