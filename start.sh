sudo yum update
sudo yum install docker
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo usermod -a -G docker ec2-user
sudo service docker start
docker -v
docker-compose -v
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
. ~/.nvm/nvm.sh
nvm install --lts
curl -o- -L https://yarnpkg.com/install.sh | bash
source ~/.bashrc
sudo yum install -y git
git clone https://github.com/22-winter-SV-bootcamp/DOH


docker-compose -f docker-compose.prod.yml up -d --build

sudo apt-get install python3-pip
sudo apt-get tzdata
dpkg-reconfigure tzdata

pip install docker

nohup python3 docker_healthcheck.py
