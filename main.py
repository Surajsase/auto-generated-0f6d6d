import json
import sys
import os
from jinja2 import Template

# Load the context data
with open('context.json', 'r') as f:
    upstream_data = json.load(f)

# Extract the newsletter from the context data
newsletter = upstream_data.get('newsletter', '')

# Define the HTML template
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Newsletter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: blue;
        }
        p {
            color: green;
        }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    {{ content | safe }}
</body>
</html>
'''

# Create a Jinja2 template object from the HTML template
template = Template(html_template)

# Render the HTML template with the newsletter data
html = template.render(title='Newsletter', content=newsletter)

# Write the rendered HTML to a file
with open('newsletter.html', 'w') as f:
    f.write(html)

print('HTML generated successfully')