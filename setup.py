import os
import json

if os.name == 'nt':
    print("Windows system detected.")
    config_dir = "C:/ProgramData/pyserver-designer"
    config_path = os.path.join(config_dir, "config.json")
    # Create directory if it doesn't exist
    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)
        print("Created config directory.")
    config = {
        "defaultAddLicence": False,
        "defaultAddLicenceType": "MIT",
        "defaultAddDefaultPage": False,
        "defaultAddDefaultPagePageName": ""
    }
    # Create file if it doesn't exist
    if not os.path.exists(config_path):
        with open(config_path, "w") as j:
            json.dump(config, j, indent=4)
        print("Created default config file.")
    else:
        with open(config_path, "r") as j:
            try:
                config = json.load(j)
            except Exception:
                print("Invalid JSON. Resetting config.")
                config = {
                    "defaultAddLicence": False,
                    "defaultAddLicenceType": "MIT",
                    "defaultAddDefaultPage": False,
                    "defaultAddDefaultPageNamePageName": ""
                }
        changed = False
        if config.get('defaultAddLicence') not in [True, False]:
            config['defaultAddLicence'] = False
            changed = True
        if config.get('defaultAddLicenceType') not in ['GPL', 'LGPL', 'MIT', 'MPL', 'APACHE']:
            config['defaultAddLicenceType'] = "MIT"
            changed = True
        if config.get('defaultAddDefaultPage') not in [True, False]:
            config['defaultAddDefaultPage'] = False
            changed = True
        if config.get('defaultAddDefaultPagePageName') is None and config.get('defaultAddDefaultPage') == True:
            config['defaultAddDefaultPagePageName'] = ""
            changed = True
        if changed:
            with open(config_path, "w") as j:
                json.dump(config, j, indent=4)
            print("Fixed config file.")
    if os.path.isdir(config_dir):
        if os.path.exists(config_path):
            print("Config file found. Checking syntax...")
            os.chdir(config_dir)
            with open("config.json", "r") as j:
                config = json.load(j)
            correct = 0
            if config['defaultAddLicence'] in [True, False]:
                correct += 25
            else:
                print("Line incorrect.")
            if config['defaultAddLicenceType'] in ['GPL', 'LGPL', 'MIT', 'MPL', 'APACHE'] and config['defaultAddLicence'] == True:
                correct += 25
            else:
                print("Line incorrect.")
            if config['defaultAddDefaultPage'] in [True, False]:
                correct += 25
            else:
                print("Line incorrect.")
            if config['defaultAddDefaultPagePageName'] is not None and config['defaultAddDefaultPage'] == True:
                correct += 25
            if correct == 100:
                print("Test passed.")
            else:
                print("Test failed.")

else:
    print("Linux/MacOS system detected.")
    config_dir = "/lib/pyserver-designer"
    config_path = os.path.join(config_dir, "config.json")
    # Create directory if it doesn't exist
    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)
        print("Created config directory.")
    config = {
        "defaultAddLicence": False,
        "defaultAddLicenceType": "MIT",
        "defaultAddDefaultPage": False,
        "defaultAddDefaultPagePageName": ""
    }
    # Create file if it doesn't exist
    if not os.path.exists(config_path):
        with open(config_path, "w") as j:
            json.dump(config, j, indent=4)
        print("Created default config file.")
    else:
        with open(config_path, "r") as j:
            try:
                config = json.load(j)
            except Exception:
                print("Invalid JSON. Resetting config.")
                config = {
                    "defaultAddLicence": False,
                    "defaultAddLicenceType": "MIT",
                    "defaultAddDefaultPage": False,
                    "defaultAddDefaultPagePageName": ""
                }
        changed = False
        if config.get('defaultAddLicence') not in [True, False]:
            config['defaultAddLicence'] = False
            changed = True
        if config.get('defaultAddLicenceType') not in ['GPL', 'LGPL', 'MIT', 'MPL', 'APACHE']:
            config['defaultAddLicenceType'] = "MIT"
            changed = True
        if config.get('defaultAddDefaultPage') not in [True, False]:
            config['defaultAddDefaultPage'] = False
            changed = True
        if config.get('defaultAddDefaultPagePageName') is None and config.get('defaultAddDefaultPage') == True:
            config['defaultAddDefaultPageNamePageName'] = ""
            changed = True
        if changed:
            with open(config_path, "w") as j:
                json.dump(config, j, indent=4)
            print("Fixed config file.")
    if os.path.isdir(config_dir):
        if os.path.exists(config_path):
            print("Config file found. Checking syntax...")
            os.chdir(config_dir)
            with open("config.json", "r") as j:
                config = json.load(j)
            correct = 0
            if config['defaultAddLicence'] in [True, False]:
                correct += 25
            else:
                print("Line incorrect.")
            if config['defaultAddLicenceType'] in ['GPL', 'LGPL', 'MIT', 'MPL', 'APACHE'] and config['defaultAddLicence'] == True:
                correct += 25
            else:
                print("Line incorrect.")
            if config['defaultAddDefaultPage'] in [True, False]:
                correct += 25
            else:
                print("Line incorrect.")
            if config['defaultAddDefaultPagePageName'] is not None and config['defaultAddDefaultPage'] == True:
                correct += 25
            if correct == 100:
                print("Test passed.")
            else:
                print("Test failed.")