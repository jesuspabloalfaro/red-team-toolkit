alias venv='python3 -m venv'
alias server='python3 -m http.server'
alias cssh="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
alias scpr="scp -P 2222 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -r"
alias pwkvpn='/opt/startpwk.sh'
alias scan='sudo $(which autorecon) -v --dirbuster.tool=gobuster --dirbuster.wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o /home/kali/Documents/pwk/results/'
alias buster='gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt'
alias uu='source ~/.zshrc'
alias navpwk='cd ~/Documents/pwk/results/'
alias own='sudo chown -R kali:kali /home/kali/Documents/pwk/'
alias enum4linux='python3 /opt/linux-tools/enum4linux-ng/enum4linux-ng.py'
alias sshpwk='ssh -p2222 -o StrictHostKeyChecking=no'
#alias proxychains='/opt/linux-tools/proxychains-ng/proxychains4'
alias combinator='/usr/lib/hashcat-utils/combinator.bin'
alias jpmount='sudo mount -t cifs -o username=smbuser,uid=$(id -u),gid=$(id -g) //10.5.0.229/smb /mnt/jp-smb'
alias cme="crackmapexec"
