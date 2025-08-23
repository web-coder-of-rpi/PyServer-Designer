# PyServerCLI
A CLI interface for creating Python-based servers.

## Building
To build, follow these steps: <br>
Create a venv:
```bash
python3 -m venv PyServer-Designer-main
```
Install packages and run setup script:
```bash
cd PyServer-Designer-main
source bin/activate
pip install pyinstaller
sudo python setup.py
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
Add to commands:
```bash
sudo mv main /bin/pysd
rm main
```
To run(after terminal is refreshed)
```bash
pysd
```
## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
This project is licensed under the MIT License.  
See [LICENSE.txt](LICENSE.txt)
