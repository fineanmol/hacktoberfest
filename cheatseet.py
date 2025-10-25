"""
A simple Python project that collects, stores, and serves cheat sheets in Markdown format.
This can be the basis for an open-source repo where contributors add cheat sheets for various topics.
"""

import os
from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory

# --- Setup ---
app = Flask(__name__)
CHEATSHEET_DIR = 'cheatsheets'
os.makedirs(CHEATSHEET_DIR, exist_ok=True)

# --- HTML Templates ---
INDEX_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cheat Sheet Repository</title>
  <style>
    body { font-family: sans-serif; margin: 2rem; background: #f9f9f9; color: #222; }
    a { color: #007bff; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .sheet { padding: 1rem; background: #fff; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin-bottom: 1rem; }
    form { margin-top: 2rem; }
    input, textarea { width: 100%; padding: 0.5rem; margin-top: 0.3rem; }
    button { padding: 0.5rem 1rem; background: #007bff; color: #fff; border: none; border-radius: 4px; }
  </style>
</head>
<body>
  <h1>📚 Cheat Sheet Repository</h1>
  <p>Contribute and browse coding cheat sheets. Perfect Hacktoberfest starter project!</p>

  <div>
    {% for sheet in sheets %}
      <div class="sheet">
        <h3>{{ sheet }}</h3>
        <a href="{{ url_for('view_sheet', name=sheet) }}">View</a>
      </div>
    {% else %}
      <p>No cheat sheets yet. Add one below!</p>
    {% endfor %}
  </div>

  <form method="post" action="/add">
    <h2>Add a new Cheat Sheet</h2>
    <label>File name (no spaces): <input type="text" name="name" required></label>
    <label>Markdown content:</label>
    <textarea name="content" rows="6" required></textarea>
    <button type="submit">Add Cheat Sheet</button>
  </form>
</body>
</html>
"""

VIEW_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ name }} Cheat Sheet</title>
  <style>
    body { font-family: sans-serif; margin: 2rem; line-height: 1.6; background: #fff; }
    pre { background: #f4f4f4; padding: 1rem; border-radius: 6px; overflow-x: auto; }
    a { color: #007bff; }
  </style>
</head>
<body>
  <a href="/">← Back</a>
  <h1>{{ name }}</h1>
  <pre>{{ content }}</pre>
</body>
</html>
"""

# --- Routes ---
@app.route('/')
def index():
    sheets = [f.replace('.md', '') for f in os.listdir(CHEATSHEET_DIR) if f.endswith('.md')]
    return render_template_string(INDEX_TEMPLATE, sheets=sheets)

@app.route('/view/<name>')
def view_sheet(name):
    path = os.path.join(CHEATSHEET_DIR, name + '.md')
    if not os.path.exists(path):
        return f"Cheat sheet '{name}' not found.", 404
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template_string(VIEW_TEMPLATE, name=name, content=content)

@app.route('/add', methods=['POST'])
def add_sheet():
    name = request.form['name'].strip()
    content = request.form['content']
    if not name:
        return "Invalid name", 400
    path = os.path.join(CHEATSHEET_DIR, name + '.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return redirect(url_for('index'))

@app.route('/download/<name>')
def download_sheet(name):
    return send_from_directory(CHEATSHEET_DIR, name + '.md', as_attachment=True)


if __name__ == '__main__':
    print("Cheat Sheet Repository running at http://127.0.0.1:5000")
    app.run(debug=True)
