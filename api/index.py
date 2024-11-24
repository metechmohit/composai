# api/index.py
from app import app

# Required for Vercel
app.debug = False

# Handle WSGI application
application = app