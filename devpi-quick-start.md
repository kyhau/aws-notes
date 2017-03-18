## devpi Quick Start Guide

For details see [Quickstart: uploading, testing, pushing releases](http://doc.devpi.net/latest/quickstart-releaseprocess.html)

#### How to add the devpi index to your pip configuration file	

Update C:\Users\username\pip\pip.ini on Windows 8/10, or ~/.config/pip/pip.conf on Linux

````sh
[global]
index_url=https://login.pw@devpi.example.com/<firstname_lastname>/dev/
````
OR
Set env variable PIP_INDEX:

````sh
set PIP_INDEX_URL=https://login.pw@devpi.example.com/<firstname_lastname>/dev/
````

Configuration file locations can be found [here](http://pip.readthedocs.org/en/stable/user_guide/)


#### How to build a wheel	

1. Update the version variable in setup.py accordingly.
2. See also the test.bat or test.sh file in your repo.
3. Then run:

    ````sh
    python setup.py bdist_wheel
    ````

#### How to add a wheel to your own devpi index	

````sh
# Login
$ devpi login <firstname_lastname> --password <pw>

# Change to your devpi index
$ devpi use https://login:pw@devpi.example.com/<firstname_lastname>/dev/

# Upload your wheel
$ devpi upload <wheel_name>.whl
````

#### How to remove a wheel from your personal devpi index	

````sh
# Login
$ devpi login <firstname_lastname> --password <pw>

# Change to your devpi index
$ devpi use https://login.pw@devpi.example.com/<firstname_lastname>/dev/

# Remove
$ devpi remove <wheel_name_with_or_without_version>
````

#### How to remove a wheel from a non-volatile, shared index

(Not recommended. Please try not to create this situation in the first place.)

````sh

# step 1: ask an admin to help. They will need ssh access to the devpi server
$ ssh admin_name@devpi.example.com

# sudo to the devpi account. This will automatically activate the appropriate python environment as well
$ sudo su devpi

# use bash's CTL+R  search to find this command with the password intact
$ devpi login root ...
$ devpi use shared/third-party

# make index editable
$ devpi index shared/third-party volatile=True

# delete the package
$ devpi remove <package_name>

# restore non-volativity
$ devpi index shared/third-party volatile=False
````

#### How to add a new user

````sh
$ devpi index <index> acl_upload=<user list>
````

#### How to add all users to a permission list

````sh
$ devpi user -l | tr "\\n" "," | xargs -i devpi index biarri/dev 'acl_upload={}'
````
