import platform
import os
import shutil


citus_extensions_path1 = "/usr/local/lib/python3.8/dist-packages/citus/citus_x/"

citus_extensions_path2 = "/usr/local/lib/python3.9/dist-packages/citus/citus_x/"

citus_extensions_path3 = "/usr/local/lib/python3.10/dist-packages/citus/citus_x/"


linux_destination = "/usr/share/"
pla = platform.system()

def if_linux1():
    if pla == "Linux":
        if os.path.isdir(citus_extensions_path1) is True:
            shutil.move(citus_extensions_path1, linux_destination)
        if os.path.isdir(citus_extensions_path1) is False and os.path.isdir("/usr/share/citus_x") is True:
            pass
        if os.path.isdir(citus_extensions_path1) and os.path.isdir("/usr/share/citus_x") is True:
            os.rmdir("/usr/share/citus_x/")
            shutil.move(citus_extensions_path1, linux_destination)
         #   pass


def if_linux2():
    if pla == "Linux":
        if os.path.isdir(citus_extensions_path2) is True:                         shutil.move(citus_extensions_path2, linux_destination)
        if os.path.isdir(citus_extensions_path2) is False and os.path.isdir("/usr/share/citus_x") is True:
            pass
        if os.path.isdir(citus_extensions_path2) and os.path.isdir("/usr/share/citus_x") is True:
            os.rmdir("/usr/share/citus_x/")
            shutil.move(citus_extensions_path2, linux_destination)
        
def if_linux3():
    if pla == "Linux":
        if os.path.isdir(citus_extensions_path3) is True:
            shutil.move(citus_extensions_path3, linux_destination)
        if os.path.isdir(citus_extensions_path3) is False and os.path.isdir("/usr/share/citus_x") is True:
            pass
        if os.path.isdir(citus_extensions_path3) and os.path.isdir("/usr/share/citus_x") is True:
            os.rmdir("/usr/share/citus_x/")
            shutil.move(citus_extensions_path3, linux_destination)

def if_linux_not_common():
    if pla == "Linux":
        if os.path.isdir(citus_extensions_path1) is False and os.path.isdir(citus_extensions_path2) is False and os.path.isdir(citus_extensions_path3) is False:
            if os.path.isdir("/usr/share/citus_x") is True:
                os.rmdir("/usr/share/citus_x/")
                os.system("git clone --quiet https://github.com/secretum-inc/citus_x /usr/share/citus_x")
            if os.path.isdir("/usr/share/citus_x") is False:
                os.system("git clone --quiet https://github.com/secretum-inc/citus_x /usr/share/citus_x")

if __name__ == "__main__":
    if_linux1()
    if_linux2()
    if_linux3()
    if_linux_not_common()
# print(dest) prints the


