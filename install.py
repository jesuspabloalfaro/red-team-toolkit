import subprocess

class Install:
    # Initializing string markers
    def __init__(self) -> None:
        self._INFO = "[*]"
        self._ERROR = "[-]"
        self._SUCCESS = "[+]"
        print(f"{self._INFO} Initializing")

    # Installing Scripts
    def install_scripts(self):
        print(f"{self._INFO} Installing Linpeas...")
        print(subprocess.run(["wget", "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh", "-o", "/opt/scripts/linpeas.sh"]))

if __name__ == '__main__':
    installer = Install()
    installer.testFunc()
