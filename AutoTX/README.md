- Recomended Using Python 3.10
- For Windows [Download Here](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe) [Scrool Down]
```
python -m pip install pip --upgrade
pip install requests
pip install web3
```
- For Termux Android [Download Here](https://f-droid.org/F-Droid.apk)
```
After Install Termux, Make Sure Allowed Permission Storage On Setting Termux
- Instal Python 3.10
pkg update && upgrade
pkg install tur-repo
pkg install python-is-python3.10
- Install Requirements
pip install --upgrade pip
pkg install -y rust binutils
CARGO_BUILD_TARGET="$(rustc -Vv | grep "host" | awk '{print $2}')" pip install maturin
pip install requests
pip install web3
```
- For Ubuntu 18.04 | 20.04 | 22.04 (VPS)
```
- Install Python 3.10
apt update && sudo apt upgrade -y
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
apt install python3.10
apt install python3-pip
- Install Requirements
pip install requests
pip install web3
```
