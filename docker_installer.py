import os

def docker_install():
  os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
  os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
  os.system('sudo apt-get update')
  os.system('apt-cache policy docker-ce')
  print("Starting Docker Installation. Docker should now be installed, the daemon started, and the process enabled to start on boot.")
  os.system('sudo apt-get install -y docker-ce')
  print("Checking that it’s running:")
  os.system('sudo systemctl status docker')
