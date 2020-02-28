import os
def faucet_downloader(permissions):
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
  inp = input('Type "sudo" if you want to give root permissions for installation\t')
  if inp == 'sudo':
    permissions = inp + ' '
  n_choice = int(input('Enter 0 if you want pip installation or 1 for apt\t'))
  if n_choice == 0:
    n = input('Input pip version enter 3 if you want to install with pip3')
    if n == '3':
      faucet_downloader_pip(permissions, n)
    else:
      faucet_downloader_pip(permissions, '')
  else:
    faucet_downloader(permissions)
  print('Installation complete')
main()
