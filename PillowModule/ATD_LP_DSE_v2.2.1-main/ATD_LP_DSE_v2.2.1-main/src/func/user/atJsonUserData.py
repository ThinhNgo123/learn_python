#!/usr/bin/env python
import sys
sys.path.insert(0,"json")
from atJsonData import atData
class atJsonUserData_Class():
    """
    Manage da
    """
    def __init__(self) -> None:
        """
        Init data of atSetting for HMI
        """
    def change_password(self,user_name, new_password):
        for user in atData.data["User"]["List"]:
            if user_name == atData.data["List"][user]["User Name"]:
                atData.data["User"]["List"][user]["Password"] = new_password
                atData.save_('User')
                print("Password is changed")
        
    def log_in(self, user_name, password):
        """
        - return : "Login successfully"
        - return : "Login failed"
        """
        for user in atData.data["User"]["List"]:
            if  (user_name == atData.data["User"]["List"][user]["User Name"]) and \
                (password == atData.data["User"]["List"][user]["Password"]) :
                # login successfully
                atData.data["User"]["User Permission"] = atData.data["User"]["List"][user]["Permission"]
                atData.data["User"]["User"] = user_name
                atData.data["User"]["Password"] = password
                atData.save('User')
                print("Login with user/password : " + user_name + "/" + password)
                print("Permission: " + atData.data["User"]["User Permission"])

        # conclude
        if atData.data["User"]["User Permission"] == "user" or  \
            atData.data["User"]["User Permission"] == "admin" :
            return "Login successfully"
        else:
            return "Login failed"
    
atJsonUserData = atJsonUserData_Class()

if __name__ == "__main__":
    atJsonUserData.reload()
    # atJsonUserData.change_password(
    #     user_name= "admin",
    #     new_password="123123"
    # )
    print(atJsonUserData.log_in(
        user_name= "ADMIN",
        password= "1234"
    ))
    print(atJsonUserData.data["User Permission"])
    # print(atJsonUserData.data)