## devpi-server Upgrade

```sh
# Login to the devpi registry server

$ sudo su devpi

# change to home directroy
cd ~
  
# check current version (or pip list)
$ devpi-server --version
 
# export devpi-server database state into PATH. This will export all users, indices (except root/pypi),
# release files, test results and documentation.
$ devpi-server --serverdir server/ --export server_old_version_exported
  
$ mv server server_old
  
# update pip to the latest version
$ pip install -U pip
  
# update devpi-server (also update devpi-common)
$ pip install -U devpi-server
  
$ pip install -U devpi-client
 
$ pip install -U devpi-web
 
# import devpi-server database from PATH where PATH is a directory which was created by a 'devpi-server
# --export PATH' operation, using the same or an earlier devpi-server version. Note that you can only import
# into a fresh server state directory (positional argument to devpi-server).
$ devpi-server --serverdir server/ --import server_old_version_exported
  
$ exit
  
# restart devpi-server
$ sudo supervisorctl restart devpi-server

```
