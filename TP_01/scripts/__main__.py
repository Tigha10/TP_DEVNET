import json
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def load_json_data_from_file(file_path):

    try :  
        f = open(file_path) # Opening JSON file
        data = json.load(f) # returns JSON object as a dict
        print(data)
        return data
    except FileNotFoundError as e: 
        print("Fichier introuvable")   
        
    
        

    pass


def load_yaml_data_from_file(file_path):
    """
        A compléter ....
    """
    pass


def render_network_config(template_name, data):

    
    template = env.get_template(template_name)
    return template.render(data) 
    
    pass

def save_built_config(file_name, data):
    """
        A compléter ....
    """
    pass


if __name__ == "__main__":
    data = load_json_data_from_file('data/R2.json')
    config = render_network_config('R2.j2',data)
    print(config)

    pass

