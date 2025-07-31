import os
import sys
class PyServerCLI:
    def __init__(self):
        # Define optional modes
        self.modes = {
            "newProject": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "openProject": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "addPage": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "editPage": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "exitProject": [],
            "deleteProject": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "setting": [
          {"pos": 1, "options":['defaultAddLicence', 'defaultAddLicenceType', 'defaultAddDefaultPageNamePageName', 'defaultAddHomePage'], "optional": False},
          {"pos": 2, "options":"any", "optional":False}
            ],
            "printProjectInfo": [],
            "deletePage": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "newStylesheet": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "editStylesheet": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "deleteStyleSheet": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "newDatabase": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "editDatabase": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "deleteDatabase": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "newScript": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "editScript": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "deleteScript": [
          {"pos": 1, "options": "any", "optional": False}
            ],
            "renamePage": [
          {"pos": 1, "options": "any", "optional": False},
          {"pos": 2, "options": "any", "optional": False}
            ],
            "renameProject": [
          {"pos": 1, "options": "any", "optional": False},
            ],
            "renameStylesheet": [
          {"pos": 1, "options": "any", "optional": False},
          {"pos": 2, "options": "any", "optional": False}
            ],
            "renameDatabase": [
          {"pos": 1, "options": "any", "optional": False},
          {"pos": 2, "options": "any", "optional": False}
            ],
            "renameScript": [
          {"pos": 1, "options": "any", "optional": False},
          {"pos": 2, "options": "any", "optional": False}
            ]
        }

    # Short for Check If Command Exists
    @staticmethod
    def checkICE(command):
        commandList = [
            'newProject', 'openProject', 'addPage', 'editPage', 'exitProject', 'deleteProject', 'setting', 'printProjectInfo', 'deletePage',
            'newStylesheet', 'editStylesheet', 'deleteStyleSheet', 'newDatabase', 'editDatabase', 'deleteDatabase',
            'newScript', 'editScript', 'deleteScript', 'renamePage', 'renameProject', 'renameStylesheet', 'renameDatabase', 'renameScript'
        ]  # List of all commands
        if command in commandList:
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
        rules = PyServerCLI.modes.get(command_name, [])

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
            PyServerCLI_Commands.{command} #type:ignore This will be added soon