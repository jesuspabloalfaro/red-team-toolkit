import subprocess
import argparse
import pwd
import os

# User Arguments
parser = argparse.ArgumentParser(
                                prog="install.py",
                                description="Common tools that every red teamer should have on their box.",
                                usage="%(prog)s [OPTIONS]")
parser.add_argument("--no-config", help="do not override existing configs", action="store_true")
args = parser.parse_args()

class Install:
    def __init__(self) -> None:
        # Setting color codes
        self._BLUE = "\033[0;34m"
        self._RED = "\033[0;31m"
        self._GREEN = "\033[0;32m"
        self._CLEAR = "\033[0m"

        # Setting info markers
        self._INFO = f"{self._BLUE}[*]{self._CLEAR}"
        self._ERROR = f"{self._RED}[-]{self._CLEAR}"
        self._SUCCESS = f"{self._GREEN}[+]{self._CLEAR}"

        # Setting global variables
        self._working_directory = os.getcwd()
        self._username = pwd.getpwuid(os.getuid())[0]
        
        print(f"{self._INFO} Initializing")

    # Installing Scripts
    def install_scripts(self):

        # Create Scripts folder
        def _create_scripts_folder():
            print(f"{self._INFO} Attempting To Create Scripts Folder...")
            os.system(f"mkdir {self._working_directory}/scripts")
            print(f"{self._SUCCESS} Created scripts folder.")
        
        _create_scripts_folder()
        
        urls = ["https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh",
                "https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany_ofs.exe",
                "https://gist.githubusercontent.com/joswr1ght/22f40787de19d80d110b37fb79ac3985/raw/50008b4501ccb7f804a61bc2e1a3d1df1cb403c4/easy-simple-php-webshell.php",
                "https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php"]
        
        script_names = ["linpeas.sh", "winPEAS.exe", "easy-php-webshell.php", "webshell.php"]

        for i in range(0,len(urls)):
            print(f"{self._INFO} Installing {script_names[i]}...")
            os.system(f'curl -L {urls[i]} -o {self._working_directory}/scripts/{script_names[i]}')
            print(f"{self._SUCCESS} {script_names[i]} Installed.")

        # Delete Duplicates (This is a bug)
        subprocess.run(["rm", "-rf", "easy-simple-php-webshell.php", "linpeas.sh", "webshell.php", "winPEASany_ofs.exe"])

    def install_packages(self):
        # Install all packages
        packages = ["villain", "python3-pip", "pipx", "openssh-client", "openssh-server", "golang-go", "python3-venv", "seclists", "curl", "dnsrecon", "enum4linux", "feroxbuster", "gobuster", "impacket-scripts", "nbtscan", "nikto", "nmap", "onesixtyone", "oscanner", "redis-tools", "smbclient", "smbmap", "snmp", "sslscan", "sipvicious", "tnscmd10g", "whatweb", "wkhtmltopdf", "git"]
        
        for i in range(0, len(packages)):
            print(f"{self._INFO} Installing {packages[i]}...")
            subprocess.run(f"sudo apt install {packages[i]} -y", shell=True)
            print(f"{self._SUCCESS} {packages[i]} Installed.")

    def install_tools(self):
        # Create tools folder
        def _create_folder():
            print(f"{self._INFO} Creating Tools Folder...")
            os.system(f'mkdir {self._working_directory}/tools')
            print(f"{self._SUCCESS} Tools folder created.")

        _create_folder()

        # Installing AutoRecon
        print(f"{self._INFO} Installing AutoRecon...")
        os.system(f'python3 -m pipx ensurepath')
        os.system("python3 -m pipx ensurepath")
        os.system(f"pipx install git+https://github.com/Tib3rius/AutoRecon.git")
        os.system("python3 -m pipx ensurepath")
        print(f"{self._SUCCESS} AutoRecon Installed.")

        # Installing NetExec
        print(f"{self._INFO} Installing NetExec...")
        os.system(f'pipx install git+https://github.com/Pennyw0rth/NetExec')
        print(f"{self._SUCCESS} NetExec Installed.")

        # Installing Ligolo-ng
        print(f"{self._INFO} Installing Ligolo-ng...")
        os.system(f'git clone https://github.com/nicocha30/ligolo-ng.git /opt/ligolo-ng')
        print(f"{self._SUCCESS} Ligolo-ng Installed.")

        # Installing PrintSpoofer64.exe
        print(f"{self._INFO} Installing PrintSpoofer64.exe...")
        os.system(f'curl -L https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe -o {self._working_directory}/tools/PrintSpoofer64.exe')
        print(f"{self._SUCCESS} PrintSpoofer64.exe Installed.")

        # Installing nc64.exe 
        print(f"{self._INFO} Installing nc64.exe...")
        os.system(f'curl -L https://raw.githubusercontent.com/int0x33/nc.exe/master/nc64.exe -o {self._working_directory}/tools/nc64.exe')
        print(f"{self._SUCCESS} nc64.exe Installed.")

        # Installing sliver 
        print(f"{self._INFO} Installing Sliver C2...")
        os.system(f"'curl https://sliver.sh/install' | sudo bash")
        print(f"{self._SUCCESS} Sliver C2 Installed.")

    def substitute_configs(self):
        configs = [".bash_aliases", ".bashrc", ".tmux.conf", ".vimrc", ".zshrc"]
        for i in range(0, len(configs)):
            print(f"{self._INFO} Attempting to change {configs[i]}...")
            os.system(f'cp {self._working_directory}/configs/{configs[i]} ~/{configs[i]}')
            print(f"{self._SUCCESS} {configs[i]} Transfered Successsfully")
        print(f"{self._INFO} Remember to Restart Your Terminal For Changes To Take Affect...")

        # Install vim style kit
        os.system(f'mkdir ~/.vim/')
        os.system(f'mkdir ~/.vim/colors/')
        os.system(f'cp {self._working_directory}/configs/deus.vim ~/.vim/colors/deus.vim')

    def change_command(self):
        # Give access to the folder to current user
        print(f"{self._INFO} Attempting to Transfer /opt/ Ownership to User {self._username}...")
        os.system(f"chown -R {self._username}:{self._username} {self._working_directory}")
        print(f"{self._SUCCESS} Ownership Changed to {self._username} Successful.")

    def enable_ssh_service(self):
        # Enable ssh service for connectivity
        print(f"{self._INFO} Attempting to enable SSH service...")
        subprocess.run("sudo systemctl enable ssh", shell=True)
        print(f"{self._SUCCESS} SSH Service Started Successfully.")
    
    def create_ssh_keys(self):
        # Create ssh keys
        print(f"{self._INFO} Attemping to create ssh keys...")
        os.system(f'mkdir ~/.ssh')
        os.system("chmod 700 ~/.ssh")
        os.system(f'ssh-keygen -b 521 -t ecdsa -f ~/.ssh/local')
        print(f"{self._SUCCESS} SSH Keys Created Successfully.")

    def install_python2_support(self):
        print(f"{self._INFO} Attemping to install pip2...")
        os.system(f'curl -L  https://bootstrap.pypa.io/pip/2.7/get-pip.py -o {self._working_directory}/scripts/get-pip.py')
        os.system(f"python2 {self._working_directory}/scripts/get-pip.py")
        os.system(f'pip2 install --upgrade setuptools')
        os.system(f"apt-get install python2-dev virtualenv -y")
        print(f"{self._SUCCESS} PIP2 Installed Successfully.")



if __name__ == '__main__':
    # Try - except for any errors
    try:
        # Define Object
        installer = Install()
        installer.install_packages()
        installer.install_scripts()
        installer.install_tools()
        installer.install_python2_support()

        if(not args.no_config):
            installer.substitute_configs()
        
        installer.enable_ssh_service()
        installer.create_ssh_keys()
    except Exception as e:
        print(f"{installer._ERROR} An exception has occured: {e}")