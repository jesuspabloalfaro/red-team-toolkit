import subprocess
import os

class Install:
    # Initializing string markers
    def __init__(self) -> None:
        self._BLUE = "\033[0;34m"
        self._RED = "\033[0;31m"
        self._GREEN = "\033[0;32m"
        self._CLEAR = "\033[0m"
        self._INFO = f"{self._BLUE}[*]{self._CLEAR}"
        self._ERROR = f"{self._RED}[-]{self._CLEAR}"
        self._SUCCESS = f"{self._GREEN}[+]{self._CLEAR}"
        print(f"{self._INFO} Initializing")

    # Installing Scripts
    def install_scripts(self):
        urls = ["https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh",
                "https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany_ofs.exe",
                "https://gist.githubusercontent.com/joswr1ght/22f40787de19d80d110b37fb79ac3985/raw/50008b4501ccb7f804a61bc2e1a3d1df1cb403c4/easy-simple-php-webshell.php",
                "https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php"]
        
        script_names = ["linpeas.sh", "winPEAS.exe", "easy-php-webshell.php", "webshell.php"]

        print(f"{self._INFO} Attempting To Create Scripts Folder...")
        os.system("su kali -c 'mkdir /opt/red-team-toolkit/scripts'")
        print(f"{self._SUCCESS} Created scripts folder.")

        for i in range(0,len(urls)):
            print(f"{self._INFO} Installing {script_names[i]}...")
            os.system(f"su kali -c 'curl -L {urls[i]} -o /opt/red-team-toolkit/scripts/{script_names[i]}'")
            print(f"{self._SUCCESS} {script_names[i]} Installed.")

        # Delete Duplicates
        subprocess.run(["rm", "-rf", "easy-simple-php-webshell.php", "linpeas.sh", "webshell.php", "winPEASany_ofs.exe"])

    def install_packages(self):
        # Update Upgrade Kali instance
        print(f"{self._INFO} Attempting to update and upgrade Kali...")
        subprocess.run(["apt", "update", "-y"])
        subprocess.run(["apt", "upgrade", "-y"])
        print(f"{self._SUCCESS} Kali Updated and Upgraded Sucessfully.")

        # Install all packages
        packages = ["python3-pip", "pipx", "openssh-client", "openssh-server", "golang-go", "python3-venv", "seclists", "curl", "dnsrecon", "enum4linux", "feroxbuster", "gobuster", "impacket-scripts", "nbtscan", "nikto", "nmap", "onesixtyone", "oscanner", "redis-tools", "smbclient", "smbmap", "snmp", "sslscan", "sipvicious", "tnscmd10g", "whatweb", "wkhtmltopdf", "git"]
        for i in range(0, len(packages)):
            print(f"{self._INFO} Installing {packages[i]}...")
            subprocess.run(["apt", "install", "-y", packages[i]])
            print(f"{self._SUCCESS} {packages[i]} Installed.")

    def install_tools(self):
        # Create tools folder
        print(f"{self._INFO} Creating Tools Folder...")
        os.system("su kali -c 'mkdir /opt/red-team-toolkit/tools'")
        print(f"{self._SUCCESS} Tools folder created.")

        # Installing AutoRecon
        print(f"{self._INFO} Installing AutoRecon...")
        os.system(f"su kali -c 'python3 -m pipx ensurepath'")
        os.system("python3 -m pipx ensurepath")
        os.system(f"pipx install git+https://github.com/Tib3rius/AutoRecon.git")
        os.system("PATH=$PATH:/root/.local/bin")
        print(f"{self._SUCCESS} AutoRecon Installed.")

        # Installing NetExec
        print(f"{self._INFO} Installing NetExec...")
        os.system(f"su kali -c 'pipx install git+https://github.com/Pennyw0rth/NetExec'")
        print(f"{self._SUCCESS} NetExec Installed.")

        # Installing Villain
        print(f"{self._INFO} Installing Villain...")
        subprocess.run(["apt", "install", "villain", "-y"])
        print(f"{self._SUCCESS} Villain Installed.")

        # Installing Ligolo-ng
        print(f"{self._INFO} Installing Ligolo-ng...")
        os.system(f"su kali -c 'git clone https://github.com/nicocha30/ligolo-ng.git /opt/ligolo-ng'")
        print(f"{self._SUCCESS} Ligolo-ng Installed.")

        # Installing PrintSpoofer64.exe
        print(f"{self._INFO} Installing PrintSpoofer64.exe...")
        os.system(f"su kali -c 'curl -L https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe -o /opt/red-team-toolkit/tools/PrintSpoofer64.exe'")
        print(f"{self._SUCCESS} PrintSpoofer64.exe Installed.")

        # Installing nc64.exe 
        print(f"{self._INFO} Installing nc64.exe...")
        os.system(f"su kali -c 'curl -L https://raw.githubusercontent.com/int0x33/nc.exe/master/nc64.exe -o /opt/red-team-toolkit/tools/nc64.exe'")
        print(f"{self._SUCCESS} nc64.exe Installed.")

    def substitute_configs(self):
        configs = [".bash_aliases", ".bashrc", ".tmux.conf", ".vimrc"]
        for i in range(0, len(configs)):
            print(f"{self._INFO} Attempting to change {configs[i]}...")
            os.system(f"su kali -c 'cp /opt/red-team-toolkit/configs/{configs[i]} ~/{configs[i]}'")
            print(f"{self._SUCCESS} {configs[i]} Transfered Successsfully")

        print(f"{self._INFO} Remember to Restart Your Terminal For Changes To Take Affect...")

    def change_command(self):
        # Give access to the folder to kali user
        print(f"{self._INFO} Attempting to Transfer /opt/ Ownership to User kali...")
        subprocess.run(["chown", "-R", "kali:kali", "/opt/"])
        print(f"{self._SUCCESS} Ownership Changed to Kali Successful.")

    def enable_ssh_service(self):
        # Enable ssh service for connectivity
        print(f"{self._INFO} Attempting to enable SSH service...")
        subprocess.run(["systemctl", "enable", "ssh"])
        print(f"{self._SUCCESS} SSH Service Started Successfully.")
    
    def create_ssh_keys(self):
        # Create ssh keys
        print(f"{self._INFO} Attemping to create ssh keys...")
        os.system("su kali -c 'mkdir ~/.ssh'")
        os.system("chmod 700 ~/.ssh")
        os.system("su kali -c 'ssh-keygen -b 521 -t ecdsa -f ~/.ssh/local'")
        print(f"{self._SUCCESS} SSH Keys Created Successfully.")


if __name__ == '__main__':
    installer = Install()
    installer.change_command()
    installer.install_packages()
    installer.install_scripts()
    installer.install_tools()
    installer.substitute_configs()
    installer.enable_ssh_service()
    installer.create_ssh_keys()