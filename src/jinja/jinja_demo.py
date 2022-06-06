from jinja2 import Template

cities = ['Berlin', 'Stockholm', 'Copenhagen']

t = Template("Hello from {{caller}}!\n\n{% for city in cities %}- {{city}}\n" "{% endfor %}")
output = t.render(caller="Me", cities=cities)

print(output)
