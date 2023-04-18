import json
from jinja2 import Template, Environment,  FileSystemLoader

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

def render_network_config(template_name, data):
    
    template = env.get_template(template_name)
    return template.render(data) 

    pass


def save_built_config(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()
    pass


def create_vlan_config_cpe_marseille():

    dataR2 = load_json_data_from_file('data/vlan_R2.json')
    configR2 = render_network_config('vlan_router.j2',dataR2)

    dataESW2 = load_json_data_from_file('data/vlan_ESW2.json')
    configESW2 = render_network_config('vlan_switch.j2',dataESW2)

    return configR2, configESW2


    pass


def create_vlan_config_cpe_paris():
    
    dataR3 = load_json_data_from_file('data/vlan_R3.json')
    configR3 = render_network_config('vlan_router.j2',dataR3)

    dataESW3 = load_json_data_from_file('data/vlan_ESW3.json')
    configESW3 = render_network_config('vlan_switch.j2',dataESW3)

    return configR3, configESW3

    pass


if __name__ == "__main__":

    r02_config, esw2_config = create_vlan_config_cpe_marseille()
    save_built_config('config/vlan_R02.conf', r02_config)
    save_built_config('config/vlan_ESW2.conf', esw2_config)
    
    r03_config, esw3_config = create_vlan_config_cpe_paris()
    save_built_config('config/vlan_R03.conf', r03_config)
    save_built_config('config/vlan_ESW3.conf', esw3_config)
