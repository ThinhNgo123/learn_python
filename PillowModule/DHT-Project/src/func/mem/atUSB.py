import sys
from time import sleep
import threading
import os

sys.path.insert(0,"json")
from atJsonData import atData

class atUSB_Class():
    USBs_Device = ["/dev/sda1","/dev/sdb1","/dev/sdc1"]
    USBs_Dir = ["/media/usb1","/media/usb2","/media/usb3"]
    USBs_Plugged = [0,0,0]
    USBs_MKDIR = [0,0,0]
    USBs_Mounted = [0,0,0]

    def __init__(self) -> None:
        # umount every usb 
        os.system("sudo umount " + self.USBs_Device[0])
        os.system("sudo umount " + self.USBs_Device[1])
        os.system("sudo umount " + self.USBs_Device[2])
        os.system("sudo rm -rf " + self.USBs_Dir[0])
        os.system("sudo rm -rf " + self.USBs_Dir[1])
        os.system("sudo rm -rf " + self.USBs_Dir[2])

        self.thread = threading.Thread(target=self._thread)
        pass

    def check_usb_plugged(self, usb_id):
        # print(os.system("sudo ls /dev/sd*"))
        try:
            os.stat(self.USBs_Device[usb_id])
            self.USBs_Plugged[usb_id] = 1
        except:
            self.USBs_Plugged[usb_id] = 0
            pass
        
        if self.USBs_Plugged[usb_id] == 1:
            # this id usb is plugged
            if self.USBs_MKDIR[usb_id] == 0:
                # if there is no made fir for this usb
                os.system("sudo mkdir " + self.USBs_Dir[usb_id])
                os.system("sudo chmod 777 " + self.USBs_Dir[usb_id])
                self.USBs_MKDIR[usb_id] = 1
                print("Create the dir " + self.USBs_Dir[usb_id])
                

            if self.USBs_Mounted[usb_id] == 0:
                #  if this id usb is not mount to its dir
                os.system("sudo mount " + self.USBs_Device[usb_id] + " " + self.USBs_Dir[usb_id])
                self.USBs_Mounted[usb_id] = 1
                print("Mount " + self.USBs_Device[usb_id] + " to the dir " + self.USBs_Dir[usb_id])

                # Read this id usb information
                self.get_usb_infor()
                atData.setGlobalNotification("Plugged USB"+str(usb_id+1))

        elif self.USBs_Plugged[usb_id] == 0:
            # this id usb is unplugged
            if self.USBs_Mounted[usb_id] == 1:
                #  if this id usb is not unmount, unmount it
                os.system("sudo umount " + self.USBs_Device[usb_id])
                self.USBs_Mounted[usb_id] = 1
                print("Unmount the " + self.USBs_Device[usb_id])        
                self.USBs_Mounted[usb_id] = 0

            if self.USBs_MKDIR[usb_id] == 1:
                # if this is usb dir is still existed, delete it
                os.system("sudo rm -rf " + self.USBs_Dir[usb_id])
                self.USBs_MKDIR[usb_id] = 0
                print("Delete the dir: " + self.USBs_Dir[usb_id])
                atData.setGlobalNotification("Unplugged USB"+str(usb_id+1))
            
            self.get_usb_infor()
        

    def details(self,usb_dir):

        disk = os.statvfs(usb_dir)

        totalBytes = float(disk.f_bsize*disk.f_blocks)
        totalGB = "%.2f GiB" % (totalBytes/1024/1024/1024)

        totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
        usedGB = " %.2f GiB" % (totalUsedSpace/1024/1024/1024)

        totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
        freeGB = "%.2f GiB" % (totalAvailSpace/1024/1024/1024)
        result = {
            "Total": totalGB,
            "Used": usedGB,
            "Free": freeGB
        }
        return result

    def get_usb_infor(self):
        # if self.USBs_Mounted !=[0,0,0]:
        for count in range(0,3):
            if(self.USBs_Mounted[count]):
                detail = self.details(self.USBs_Dir[count])
                atData.data["Memory"]["USB"][str(count+1)]['Status'] = 'Mounted'
                atData.data["Memory"]["USB"][str(count+1)]["Name"] = '...'
                atData.data["Memory"]["USB"][str(count+1)]["Total"] = detail["Total"]
                atData.data["Memory"]["USB"][str(count+1)]["Used"] = detail["Used"]
                atData.data["Memory"]["USB"][str(count+1)]["Free"] = detail["Free"]
            else:
                atData.data["Memory"]["USB"][str(count+1)]['Status'] = 'Unmounted'
                atData.data["Memory"]["USB"][str(count+1)]["Name"] = '...'
                atData.data["Memory"]["USB"][str(count+1)]["Total"] = '...'
                atData.data["Memory"]["USB"][str(count+1)]["Used"] = '...'
                atData.data["Memory"]["USB"][str(count+1)]["Free"] = '...'
        
        atData.save("Memory")
    
    def _thread(self):
        while 1:
            self.check_usb_plugged(0)
            sleep(1)
            self.check_usb_plugged(1)
            sleep(1)
            self.check_usb_plugged(2)
            sleep(1)
            

atUSB = atUSB_Class()

if __name__ == "__main__":
    atUSB.thread.start()