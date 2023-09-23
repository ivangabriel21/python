from os import system
import subprocess

system("apt update -y && apt upgrade -y")
system("apt install wget -y && apt-get install openssh-server -y")
system("service ssh start")
system("wget -P /root/ https://raw.githubusercontent.com/ivangabriel21/DependeciaDX/main/sshd_config")
system("rm -rf /etc/ssh/sshd_config")
system("mv /root/sshd_config /etc/ssh/")
system("service ssh restart")
new_password = "ivangabriel"
change_password_cmd = f"echo 'root:{new_password}' | sudo chpasswd"
subprocess.run(change_password_cmd, shell=True)
system("wget -P /root https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz")
system("tar -xzvf /root/ngrok-v3-stable-linux-amd64.tgz")
system("/root/./ngrok config add-authtoken 2VaL3LAsgw2R7Hl46qj2TbJ5fCr_2NsVnR9cxV9SQRk6dm6hR")
system("/root/./ngrok tcp 2223")
