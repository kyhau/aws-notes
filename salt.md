# SaltStack

```
# Test a command
sudo salt myserver state.highstate test=True

# Apply changes to a server
sudo salt -L myserver1,myserver2 state.highstate

sudo salt myserver state.highstate --state-output=changes

sudo salt myserver state.apply pkgs.unattended-upgrades --state-output=changes

# Override pillar value	
sudo salt '*' state.apply myserver pillar='{"ftpusername": "test", "ftppassword": "hello"}'

sudo salt '*' cmd.run 'samba --version'

sudo salt-key -L

sudo salt-run manage.status

# Check accepted/unaccepted/rejected minion keys
salt-key -L

# Accept all new minion keys
salt-key -A

# Accept a specific minion key	
salt-key -a <minion-key>

sudo stop salt-minion
sudo salt-minion -l debug

# If you change the hostname of a salt-minion	
# Stop the service : sudo service salt-minion stop
# Edit the hostname in /etc/salt/minion_id
# Start the service again 
```

## Salt-master ports

- 4505 : publsh_port - The network port to set up the publication interface.
- 4506 : ret_port - The port used by the return server, this is the server used by Salt to receive execution returns
  and command executions.

Add these port to the Security Group of a salt-master instance. 
