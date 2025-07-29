import os
import sys
class PyServerCLI:
    def __init__(self):
        # Define optional modes
        self.oModes = {
     "echo": [
        {"pos": 1, "options": ['display', 'show', 'print'], "optional": True},
      ]
    }

    # Define required modes
        self.rModes = {
      "echo": [
        {"pos": 2, "options": "any", "optional": False},
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

    