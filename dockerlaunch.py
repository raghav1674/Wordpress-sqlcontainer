import os
from time import sleep

os.system("clear")
os.system("tput setaf 3")
print("           WELCOME TO WORDPRESS-CONTAINER WORLD  ")
print("           ---------------------------------   ")
os.system("tput setaf 7")
image=input("Enter the sqlimage name: ")
mysql_rootpass=input("Enter the mysql root pass: ")
mysql_user=input("Enter the mysql username: ")
mysql_database=input("Enter the database name: ")
mysql_password=input(f"Enter the mysql password for {mysql_user}: ")
wordpressimage=input("Enter the Wordpressimage name: ")
host_port=input("Enter the port of host to be exposed :")
docker_port=input("Enter the port where ur server is running :")
network=input("Enter the network name :")
os.system("tput setaf 4")
print("   creating a network with driver as bridge")
os.system("tput setaf 7")
os.system(f" docker  network create {network}")
basedock=f"{host_port}:{docker_port}"
with open(".env","w") as ef:
    ef.write(f"basedock={basedock}\n")
    ef.write(f"networkname={network}:\n")
    ef.write(f"wordpressimage={wordpressimage}\n")
    ef.write(f"imagename={image.rstrip()}\n")
    ef.write(f"mysql_rp={mysql_rootpass}\n")
    ef.write(f"mysql_uname={mysql_user}\n")
    ef.write(f"mysql_dbname={mysql_database}\n")
    ef.write(f"mysql_pass={mysql_password}\n")
os.system("tput setaf 5")
print("============ launching wordpress-sql containers ===============")
os.system("tput setaf 7")
os.system(" docker-compose up -d")

print(f"service running at  http://192.168.29.62:{host_port}")












