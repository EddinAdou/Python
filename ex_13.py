import socket
hote_name = socket.gethostname()
print(hote_name)

ip_adress = socket.gethostbyname(hote_name)
print(ip_adress)

# afficher l'architecture du processeur de la machine
import platform
print(platform.architecture())
# afficher le nom de la machine
import platform
print(platform.machine())
# afficher le nom du système d'exploitation
import platform
print(platform.system())
# afficher la version du système d'exploitation
import platform
print(platform.version())
