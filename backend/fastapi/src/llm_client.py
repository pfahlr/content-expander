import openai
from jinja2 import Template
from pathlib import Path

def render_prompt(template_name, **context):
    template = Template(Path(fprompts/{template_name}.txt).read_text())
    return template.render(**context)

def generate_outputs(title, content, outputs):
    results = {}
    for out in outputs:
        prompt = render_prompt(out, title=title, content=content)
        res = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{role: user, content: prompt}]
        )
        results[out] = res['choices'][0]['message']['content']
    return results

