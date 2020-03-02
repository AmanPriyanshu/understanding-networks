import os
os.system('cd ~')
a = int(input('Enter 0 or 1, 0 for Normal and 1 for Controller:\t'))
name = input('Enter the name of docker-name:\t')
if a == 0:
	os.system('sudo docker run -it --name '+name+' --network=none busybox /bin/sh')
else:
	os.system('sudo docker run -it --name faucetctl --network=host faucet/faucet /bin/bash')