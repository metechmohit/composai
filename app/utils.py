import markdown
from slugify import slugify

def format_content(content):
    # Convert markdown to HTML
    html_content = markdown.markdown(content)
    return html_content

def create_slug(text):
    return slugify(text)