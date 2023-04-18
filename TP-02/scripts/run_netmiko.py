import json
from netmiko import ConnectHandler

def question_9(net_connect):
    print(net_connect.__dict__)
    pass

def question_10(net_connect):
    command = "show ip int brief"
    output= net_connect.send_command(command)
    print(output)
    pass

def question_11(net_connect):
    command = "show ip int brief"
    output= net_connect.send_command(command, use_textfsm=True)
    print(output)
    pass


def question_12(net_connect):
    command = "show ip route"
    output= net_connect.send_command(command, use_textfsm=True)
    print(output)
    pass

def question_13(net_connect):
    command = "show ip int brief"
    command2 = "show run int"
    
    output= net_connect.send_command(command, use_textfsm=True)
    print(output)
    for i in output :
        interface = i['intf']
        output2= net_connect.send_command(command2 +' '+interface, use_textfsm=True)
        print(output2)

    pass


def question_14(net_connect):
    commands = ["int lo1","ip add 192.168.1.1 255.255.255.255","description loopback interface from netmiko"]
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()
    print(output)
    pass


def question_15(net_connect):
    commands = ["no int lo1"]
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()
    print(output)
    pass

def question_16(net_connect):
    cfg_file = "config/loopback_R01.conf"
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()

    print()
    print(output)
    print()
    pass


def question_17(net_connect):
   
        commands=["no int lo1", "no int lo2", "no int lo3", "no int lo4"]
        output = net_connect.send_config_set(commands)
        output += net_connect.save_config()
        print(output)
        pass


def get_inventory():
    try :  
        f = open("inventory/hosts.json") # Opening JSON file
        data = json.load(f) # returns JSON object as a dict
        #print(data)
        return data
    except FileNotFoundError as e: 
        print("Fichier introuvable") 
    pass


def question_20():

    try :  
        f = open("inventory/hosts.json") # Opening JSON file
        data = json.load(f) # returns JSON object as a dict
        
        for device in data : 
            
            if device['hostname'] != "R1" and device['hostname'] != "ESW1":
                name = {
                        'device_type': device.get("device_type"),
                        'host': device.get("ip"),
                        'username': device.get("username"),
                        'password': device.get("password")
                    }
                net_connect = ConnectHandler(**name)
                command = "show ip int brief"
                command2 = "show run int" 
    
                output= net_connect.send_command(command, use_textfsm=True)
                
                for i in output :
                    interface = i['intf']
                    if interface == "GigabitEthernet0/0.99" :
                        output2= net_connect.send_command(command2 +' '+interface, use_textfsm=True)
                        print(output2)

        #print(data)
        
    except FileNotFoundError as e: 
        print("Fichier introuvable") 
    pass


def question_21():

    try :  
        f = open("inventory/hosts.json") # Opening JSON file
        data = json.load(f) # returns JSON object as a dict
        
        for device in data : 
            if device['hostname'] != "R1" and device['hostname'] != "ESW1":
                name = {
                        'device_type': device.get("device_type"),
                        'host': device.get("ip"),
                        'username': device.get("username"),
                        'password': device.get("password")
                    }
                print(name)
                net_connect = ConnectHandler(**name)
                cfg_file = "config/vlan_{0}.conf".format(device.get('hostname'))
                print(cfg_file)
                output = net_connect.send_config_from_file(cfg_file)
                output += net_connect.save_config()
                
                print(output)


        
        
    except FileNotFoundError as e: 
        print("Fichier introuvable") 
    pass
    

if __name__ == "__main__":   

    r01 = {
        'device_type': 'cisco_ios',
        'host':   '172.16.100.62',
        'username': 'cisco',
        'password': 'cisco'
    }
    net_connect = ConnectHandler(**r01)
    
    #question_9(net_connect)
    #question_10(net_connect)
    #question_11(net_connect)
    #question_12(net_connect)
    #question_13(net_connect)
    #question_14(net_connect)
    #question_15(net_connect)
    #question_16(net_connect)
    #question_17(net_connect)
    #hosts = get_inventory()
    #print(hosts)
    #question_20()
    question_21()