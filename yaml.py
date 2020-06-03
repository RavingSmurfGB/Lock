from pathlib import Path
import yaml

def openvars():
    variables['card'] = 0
    if Path('vars.yaml').is_file():
        with open("vars.yaml", 'r') as f:
            variables = yaml.safe_load(f)
    return variables['card']

def setvars(card):
    with open("vars.yaml", 'w', encoding='utf8') as f:
        variables = {}
        variables['card'] = card
        f.write(yaml.dump(variables))



