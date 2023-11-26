import pathlib
import subprocess

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
        print(f"{self._INFO} Installing Linpeas...")
        try:
            subprocess.run(["wget", "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh", "-o", f"{pathlib.Path().resolve()}/scripts/linpeas.sh"])
            print(f"{self._SUCCESS} Linpeas Installed.")
        except:
            print(f"{self._ERROR} There was an error in the installation.")

if __name__ == '__main__':
    installer = Install()
    installer.install_scripts()
