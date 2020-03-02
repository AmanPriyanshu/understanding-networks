import os
def faucet_downloader(permissions):
  permissions = 'sudo'
  os.system(permissions+'apt-get install curl gnupg apt-transport-https lsb-release')
  os.system('echo "deb https://packagecloud.io/faucetsdn/faucet/$(lsb_release -si | awk \'{print tolower($0)}\')/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/faucet.list')
  os.system('curl -L https://packagecloud.io/faucetsdn/faucet/gpgkey | sudo apt-key add -')
  os.system(permissions+'apt-get update')
  os.system(permissions+'apt-get install faucet-all-in-one')
  
def faucet_downloader_pip(permissions, n):
  os.system(permissions+'apt-get install python3-dev python3-pip')
  os.system('pip'+str(n)+' install setuptools')
  os.system('pip'+str(n)+' install wheel')
  os.system('pip'+str(n)+' install faucet')

def main():
  faucet_downloader_pip('sudo ', '3')
main()
