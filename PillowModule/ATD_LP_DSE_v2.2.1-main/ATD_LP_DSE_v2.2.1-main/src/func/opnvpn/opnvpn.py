import os
import threading
# os.system("openvpn --config Dataloger_OPZ2_Prototype.ovpn")

# Get the list of all files and directories
path = "configs"
dir_list = os.listdir(path)
print("OpenVPN config files:")
for config in dir_list:
    print(config)
# prints all files
for config in dir_list:
    def _thread():
         os.system("openvpn --config configs/" + config)
    threading.Thread(target = _thread).start()
    