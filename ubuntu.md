# Ubuntu

```
################################################################################
# xargs 
cat dirs | xargs mkdir

################################################################################
# umount
umount -l -f /var/docker-kingkong

################################################################################
# Free memory
#   You can free up unused memory under Ubuntu/Linux Mint using this command:
#   NOTE: this action won't make your system faster nor it will affect its
#   stability and performance, it will just clean up memory used by the Linux
#   Kernel on caches.

sudo sysctl -w vm.drop_caches=3

# Free up memory either used or cached (page cache, inodes, and dentries):
#   NOTE: You can use cron jobs to schedule the commands above to run at specific time intervals.

sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

################################################################################
# List all users
cut -d: -f1 /etc/passwd

################################################################################
# apt

apt list --installed | grep gdal

# Show lib
strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX

################################################################################
# Check local cert expiry date (e.g. on dantzig)

openssl x509 -enddate -noout -in /home/path/my_cert.pem

################################################################################
# Check the MAC address on server

ifconfig | grep HWaddr

################################################################################
watch -n no_of_seconds cmd

################################################################################
# https://community.home-assistant.io/t/ha-0-58-1-cant-start-loaded-not-found-reason-no-such-file-or-directory/33669/3
# If see error like:
#   Loaded: not-found (Reason: No such file or directory)
#   Active: inactive (dead)  
# Then run

sudo systemctl --system daemon-reload

################################################################################
# Copy files from ubuntu to windows using psftp

psftp: no hostname specified; use "open host.name" to connect
psftp> open 12.34.256.78
login as: <username>
Remote working directory is /home/<username>
psftp> get mycsvfile.csv
remote:/home/<username>/mycsvfile.csv => local:mycsvfile.csv
psftp> get mycsvfile.csv "C:\Users\<username>\Documents\mycsvfile.csv"
remote:/home/<username>/mycsvfile.csv => local:C:\Users\<username>\Documents\mycsvfile.csv

################################################################################
# Adding ssh key (https://help.github.com/articles/generating-ssh-keys/)

ls -al ~/.ssh

ssh-keygen -t rsa -C "uname@example.com"
eval "$(ssh-agent)"
ssh-add ~/.ssh/id_rsa

#copy to clipboard
cat ~/.ssh/id_rsa.pub

################################################################################
cowsay -l

cowsay "hello, I'm a cow"
fortune | cowsay
fortune | cowsay -f tux
fortune | cowsay -f suse

echo 'destroy him!' | cowsay -f
echo 'destroy him!' | cowsay -f /usr/share/cows/surgery.cow

```