import os
import zipfile

project_name = "springlake_website"
folders = [
    f"{project_name}/static",
    f"{project_name}/templates"
]

files_content = {
    f"{project_name}/app.py": '''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/classes')
def classes():
    return render_template("classes.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
''',

    f"{project_name}/static/style.css": '''body {
    font-family: Arial;
    background-color: #f0f8ff;
    margin: 0;
    padding: 0;
}
nav {
    background-color: #0066cc;
    color: white;
    padding: 10px;
}
nav a {
    color: white;
    margin-right: 15px;
    text-decoration: none;
}
.content {
    padding: 20px;
}
''',

    f"{project_name}/templates/base.html": '''<!DOCTYPE html>
<html>
<head>
    <title>Springlake School</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/classes">Classes</a>
        <a href="/contact">Contact</a>
    </nav>
    <div class="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
''',

    f"{project_name}/templates/home.html": '''{% extends "base.html" %}

{% block content %}
<h1>Welcome to Springlake School</h1>
<p>We help children learn and grow.</p>
{% endblock %}
''',

    f"{project_name}/templates/about.html": '''{% extends "base.html" %}

{% block content %}
<h1>About Us</h1>
<p>Springlake School is dedicated to providing quality education to children.</p>
{% endblock %}
''',

    f"{project_name}/templates/classes.html": '''{% extends "base.html" %}

{% block content %}
<h1>Our Classes</h1>
<ul>
    <li>Math</li>
    <li>Science</li>
    <li>English</li>
    <li>Art</li>
</ul>
{% endblock %}
''',

    f"{project_name}/templates/contact.html": '''{% extends "base.html" %}

{% block content %}
<h1>Contact Us</h1>
<p>Email: contact@springlakeschool.edu</p>
<p>Phone: (555) 123-4567</p>
{% endblock %}
'''
}

# Create folders and write files
for folder in folders:
    os.makedirs(folder, exist_ok=True)
for filepath, content in files_content.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Create ZIP file
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for filepath in files_content.keys():
        zipf.write(filepath)
        os.remove(filepath)
    for folder in reversed(folders):
        os.rmdir(folder)

print(f"{zip_filename} created successfully.")
