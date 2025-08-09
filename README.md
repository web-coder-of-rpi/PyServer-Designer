# PyServerCLI
A CLI interface for creating Python-based servers.

## Building
To build, follow these steps: <br>
Create a venv:
```bash
python3 -m venv PyServer-Designer-main
```
Install packages:
```bash
cd PyServer-Designer-main
source bin/activate
pip install pyinstaller
```
Build binary file:
```bash
pyinstaller --onefile main.py
```
Run binary file:
```bash
cd dist
sudo chmod u+x main
./main
```
## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
This project is licensed under the MIT License.  
See [LICENSE.txt](LICENSE.txt)
