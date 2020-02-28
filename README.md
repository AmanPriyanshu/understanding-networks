# understanding-networks
Trying to understand Networks and their Implementation

## Clone repository:
Run "git clone https://github.com/AmanPriyanshu/understanding-networks.git ." inside the folder where you want to clone this repository.

## Install Faucet Quickly:
Run "python faucet_installer.py" in the folder where the repository has been cloned to.

## Faucet Confgiuration:
1. Poseidon requires at least Faucet version 1.8.6 or higher.
2. Unless Poseidon and Faucet are running on the same host, Poseidon will connect to Faucet using SSH. So you'll need to create an account that can SSH to the machine running Faucet and that has rights to modify the configuration file faucet.yaml
3. currently Poseidon expects it to be in the default /etc/faucet/faucet.yaml location and dps must all be defined in faucet.yaml for Poseidon to update the network posture correctly.
4. If you have Faucet running already, make sure Faucet is started with the following environment variables, which allow Poseidon to change its config and recieve faucet events.
```
export FAUCET_EVENT_SOCK=1
export FAUCET_CONFIG_STAT_RELOAD=1
```
