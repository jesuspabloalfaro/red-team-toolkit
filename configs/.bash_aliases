alias venv='python3 -m venv'
alias server='python3 -m http.server'
alias scan='sudo /root/.local/bin/autorecon -v --dirbuster.wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o /home/kali/Documents/scan/'
alias uu='source ~/.zshrc'
alias own='sudo chown -R kali:kali /home/kali/Documents/scan/'
alias jpmount='sudo mount -t cifs -o username=smbuser,uid=$(id -u),gid=$(id -g) //10.5.0.229/smb /mnt/jp-smb'
