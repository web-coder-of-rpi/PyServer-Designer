import os
import json
import licences

class PyServerCLI:
    # Define optional modes as a class variable
    modes = {
        "newProject": {
            "description": "Create a new project at the specified path.",
            "args": [
                {"pos": 1, "options": "any", "optional": False},
                {"pos": 2, "options": ['MPL', 'LGPL', 'GPL', 'MIT', 'APACHE']}
            ]
        },
        "openProject": {
            "description": "Open an existing project from the specified path.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "addPage": {
            "description": "Add a new page to the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "editPage": {
            "description": "Edit an existing page in the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "exitProject": {
            "description": "Exit the current project.",
            "args": []
        },
        "deleteProject": {
            "description": "Delete the specified project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "setting": {
            "description": "Set or get a project setting.",
            "args": [
                {"pos": 1, "options": ["defaultAddLicence", "defaultAddLicenceType", "defaultAddDefaultPagePageName", "defaultAddDefaultPage"], "optional": False},
                {"pos": 2, "options": "any", "optional": False}
            ]
        },
        "printProjectInfo": {
            "description": "Print information about the current project.",
            "args": []
        },
        "deletePage": {
            "description": "Delete a page from the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "newStylesheet": {
            "description": "Create a new stylesheet for the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "editStylesheet": {
            "description": "Edit an existing stylesheet.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "deleteStyleSheet": {
            "description": "Delete a stylesheet from the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "newDatabase": {
            "description": "Create a new database for the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "editDatabase": {
            "description": "Edit an existing database.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "deleteDatabase": {
            "description": "Delete a database from the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "newScript": {
            "description": "Create a new script for the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "editScript": {
            "description": "Edit an existing script.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "deleteScript": {
            "description": "Delete a script from the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "renamePage": {
            "description": "Rename a page in the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False},
                {"pos": 2, "options": "any", "optional": False}
            ]
        },
        "renameProject": {
            "description": "Rename the current project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False}
            ]
        },
        "renameStylesheet": {
            "description": "Rename a stylesheet in the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False},
                {"pos": 2, "options": "any", "optional": False}
            ]
        },
        "renameDatabase": {
            "description": "Rename a database in the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False},
                {"pos": 2, "options": "any", "optional": False}
            ]
        },
        "renameScript": {
            "description": "Rename a script in the project.",
            "args": [
                {"pos": 1, "options": "any", "optional": False},
                {"pos": 2, "options": "any", "optional": False}
            ]
       },
       "help": {
           "description": "Show desription for a command.",
           "args": [
               {"pos": 1, "options": "any", "optional": True}
           ]
       }
    }
    commandList = [
            'newProject', 'openProject', 'addPage', 'editPage', 'exitProject', 'deleteProject', 'setting', 'printProjectInfo', 'deletePage',
            'newStylesheet', 'editStylesheet', 'deleteStyleSheet', 'newDatabase', 'editDatabase', 'deleteDatabase',
            'newScript', 'editScript', 'deleteScript', 'renamePage', 'renameProject', 'renameStylesheet', 'renameDatabase', 'renameScript', 'help'
        ]  # List of all commands

    # Short for Check If Command Exists
    @staticmethod
    def checkICE(command):
        if command in PyServerCLI.commandList:
            return 0  # Command does exist
        else:
            return 1  # Command does not exist
        
    @staticmethod
    def commandArgsCheck(command):
        cmd = command.strip().split()
        command_name = cmd[0]

        if PyServerCLI.checkICE(command_name) == 1:
            return 1 # Error 1: ICE check failed (command not recognized)

        args = cmd[1:]  # everything after the command
        mode = PyServerCLI.modes.get(command_name, None)
        if not mode:
            return 1 # Error 1: Command not recognized (should not happen if checkICE is correct)
        rules = mode.get('args', [])

        for i, rule in enumerate(rules):
            if i >= len(args):
                if not rule.get("optional", False):
                    return 2  # Error 2: Missing required argument
                else:
                    continue  # optional and missing is OK
            value = args[i]
            allowed = rule["options"]
            if allowed != "any" and value not in allowed:
                return 3  # Error 3: Invalid argument value

        # Args are correct
        return 0

    @staticmethod
    def runCommand(command):
        code = PyServerCLI.commandArgsCheck(command)
        if code == 1:
            return 1
        elif code == 2:
            return 2
        elif code == 3:
            return 3
        else:
            cmd = command.strip().split()
            func_name = cmd[0]
            args = cmd[1:]
            func = getattr(PyServerCLI_commands(), func_name, None)
            if callable(func):
                return func(*args)
            else:
                raise AttributeError(f"Function '{func_name}' not found in PyServerCLI_commands.")

class PyServerCLI_commands():
    @staticmethod
    def help(command=None):
        if command is None or command.strip() == "":
            for c in PyServerCLI.commandList:
                print(f"{c}: {PyServerCLI.modes[c]['description']}")
        else:
            if PyServerCLI.checkICE(command) == 1:
                print("Command does not exist.")
            else:
                print(f"{command}: {PyServerCLI.modes[command]['description']}")

    @staticmethod
    def newProject(project_path, licence=None):
        project_name = os.path.basename(project_path)
        root_path = os.path.dirname(project_path)
        os.makedirs(project_path, exist_ok=True)
        os.chdir(project_path)
        folders = ['pages', 'scripts', 'stylesheets', 'databases', 'other']
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        with open(".pysdproject", "w") as p:
            p.write("f0.0.1")
        with open("runserver.py", "w") as r:
            content = f"""
#--------------------------------------{project_name}--------------------------------------#
This is a PyServer-Designer Project. (https://github.com/web-coder-of-rpi/PyServer-Designer)
#------------------------------------------------------------------------------------------#
import flask

            """
            r.write(content)
        with open("README.md", "w") as m:
            content = f"""
# {project_name}

            """
            m.write(content)

        # Handle config and license
        if os.name == "nt":
            config_path = "C:/ProgramData/pyserver_designer/config.json"
        else:
            config_path = os.path.expanduser("~/.config/pyserver_designer/config.json")

        if os.path.exists(config_path):
            with open(config_path, "r") as j:
                config = json.load(j)
            # Handle license
            if not config.get('defaultAddLicence', False):
                if licence is None:
                    print("Please specify licence type.")
                elif licence in ['GPL', 'LGPL', 'MIT', 'MPL', 'APACHE']:
                    if licence == "GPL":
                        wlicence = licences.gnu_gpl_three()
                    elif licence == "LGPL":
                        wlicence = licences.gnu_lgpl_three()
                    elif licence == "MIT":
                        wlicence = licences.mit()
                    elif licence == "MPL":
                        wlicence = licences.mpl()
                    elif licence == "APACHE":
                        wlicence = licences.apache()
                    else:
                        wlicence = ""
                    if wlicence:
                        with open("LICENSE", "w") as lic:
                            lic.write(wlicence)
            # Handle default page
            if config.get('defaultAddDefaultPage') and config.get('defaultAddDefaultPagePageName'):
                page_name = config['defaultAddDefaultPagePageName']
                pages_dir = os.path.join(project_path, "pages")
                page_path = os.path.join(pages_dir, page_name)
                if not os.path.exists(page_path):
                    with open(page_path, "w") as f:
                        f.write("")
        print("Project generated.")

class CLI:
    @staticmethod
    def run():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(f"PyServer Designer CLI")
        print("Type 'help' for a list of commands. Use 'exit' or 'quit' to exit the CLI.")
        while True:
            command = input("PyServer> ")  
            if command.lower() in ['exit', 'quit']:
                print("Exiting PyServer Designer CLI.")
                break
            elif command.lower() in ['erase', 'clear']:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                continue  # Just clear and continue, don't break or recurse
            try:
                result = PyServerCLI.runCommand(command)
                if result == 1:
                    print("Error: Command not recognized.")
                elif result == 2:
                    print("Error: Missing required argument.")
                elif result == 3:
                    print("Error: Invalid argument value.")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please check your syntax and try again.")

CLI.run()