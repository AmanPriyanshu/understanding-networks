import os
def poseidon_installation():
  os.system('curl -L https://raw.githubusercontent.com/CyberReboot/poseidon/master/bin/poseidon -o /usr/local/bin/poseidon')
  os.system('chmod +x /usr/local/bin/poseidon')
