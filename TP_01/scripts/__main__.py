import json
import yaml
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
    
    data = yaml.safe_load(open(file_path))
    print(data)

    return data
    pass


def render_network_config(template_name, data):

    
    template = env.get_template(template_name)
    return template.render(data) 
    
    pass

def save_built_config(file_name, data):
    
    f = open(file_name, "w")
    f.write(data)
    f.close()

    pass


if __name__ == "__main__":
    dataR2 = load_json_data_from_file('data/R2.json')
    configR2 = render_network_config('R2.j2',dataR2)
    save_built_config('config/R2.conf', configR2)

    dataESW2 = load_json_data_from_file('data/ESW2.json')
    configESW2 = render_network_config('ESW2.j2',dataESW2)
    save_built_config('config/ESW2.conf', configESW2)

    dataR2_yaml = load_yaml_data_from_file('data/R2.yaml')
    configR2_yaml = render_network_config('R2.j2',dataR2_yaml)
    save_built_config('config/R2_from_yaml.conf', configR2_yaml)

    dataESW4_yaml = load_yaml_data_from_file('data/ESW4.yaml')
    configESW4_yaml = render_network_config('ESW2.j2',dataESW4_yaml)
    save_built_config('config/ESW4_from_yaml.conf', configESW4_yaml)


    pass

