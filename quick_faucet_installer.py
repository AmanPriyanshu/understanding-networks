import os
def faucet_downloader():
  os.system('sudo apt-get install curl gnupg apt-transport-https lsb-release
  os.system('echo "deb https://packagecloud.io/faucetsdn/faucet/$(lsb_release -si | awk \'{print tolower($0)}\')/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/faucet.list')
  os.system('curl -L https://packagecloud.io/faucetsdn/faucet/gpgkey | sudo apt-key add -')
  os.system('sudo apt-get update')
  os.system('sudo apt-get install faucet-all-in-one')

faucet_downloader()
