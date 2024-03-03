# Red-Team-Toolkit
A collection of scripts and tools I typically install on fresh Kali
virtual machines. I created this repo for myself and others to use
to quickly format their Kali machines without having to manually
look everything up. Hope you enjoy!

# Tools
- [AutoRecon](https://github.com/Tib3rius/AutoRecon)
- [NetExec](https://github.com/Pennyw0rth/NetExec)
- [Villain](https://github.com/t3l3machus/Villain)
- [Ligolo-ng](https://github.com/nicocha30/ligolo-ng)
- [nc64.exe](https://github.com/int0x33/nc.exe/)
- [PrintSpoofer64.exe](https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe)
- [Rubeus.exe](https://github.com/GhostPack/Rubeus)
- [SharpHound.exe](https://github.com/BloodHoundAD/SharpHound/releases/tag/v2.0.1)


# Scripts
- [Linpeas](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)
- [Winpeas](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)
- [Simple PHP Webshell](https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985)
- [PHP Webshell](https://github.com/WhiteWinterWolf/wwwolf-php-webshell)
- [FodHelperBypass.ps1](https://github.com/winscripting/UAC-bypass/blob/master/FodhelperBypass.ps1)

# Configs
- Tmux
- Vim 
- Bashrc
- Bash_Aliases


# Installation Instructions
1) Update and Upgrade your current system while installing python + virtual environment + pip
```sudo apt update -y && sudo apt upgrade -y && sudo apt install python3 python3-venv python3-pip```

2) Clone the repository in any directory of your choosing
```git clone https://github.com/jesuspabloalfaro/red-team-toolkit.git```

3) Navigate to the repository
```cd red-team-toolkit```

4) Create a virtual environment
```python3 -m venv venv```

5) Activate your virtual environment
```source venv/bin/activate```

6) Install the required dependencies
```pip3 install -r requirements.txt``` 

7) Install the tools and scripts. You will be prompted to enter your password for SUDO privileges at times.
```python3 install.py [OPTIONS]```
*Reference Script Arugments below to view the full list of options.*

# Common Usages
## Script Arguments
```--no-config```
Flag that stops my personal configs from overriding your existing configs.
If you choose to use my configs, do not set this flag.

## Autorecon
Autorecon is a great tool to do alot of enumeration for CTF's. Rather than pass lots of arguments to autorecon,
you can simply run the alias `scan {IP_ADDRESS}` to have my personal autorecon flags set. The default location
to where the scan results are stored are in `/home/kali/Documents/scan` 

# TODO
- Create error checking in installer
- Create modularity