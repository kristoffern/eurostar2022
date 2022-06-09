"""
	Example code showing how you can use a templating engine like Jinja
	to create reusable templates for messages and text.
	Normally the templates exists outside in .html files
"""

from jinja2 import Template

cities = ['Berlin', 'Stockholm', 'Copenhagen']

t = Template("Hello from {{caller}}!\n\n{% for city in cities %}- {{city}}\n" "{% endfor %}")
output = t.render(caller="Me", cities=cities)

print(output)
