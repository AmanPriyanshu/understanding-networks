# Installers:
## docker_installer:

#### Followed tutorial from: https://www.hostinger.in/tutorials/how-to-install-and-use-docker-on-ubuntu/

#### Refer code documentation for further clarification. However it simply downloads and installs #### Docker from:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Since it auto-installs it. It allows for easier use and access for the implementer.
