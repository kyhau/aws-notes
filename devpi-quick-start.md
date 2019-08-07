# devpi Quick Start Guide

For details see [Quickstart: uploading, testing, pushing releases](
http://doc.devpi.net/latest/quickstart-releaseprocess.html)

## How to add the devpi index to your pip configuration file	

Update C:\Users\username\pip\pip.ini on Windows 8/10, or ~/.config/pip/pip.conf on Linux

```
[global]
index_url=https://<uname>>:<upass>@devpi.mycompany.com/<uname>/dev/
```
OR
Set env variable PIP_INDEX:

```
set PIP_INDEX_URL=https://<uname>:<upass>@devpi.mycompany.com/<uname>/dev/
```

Configuration file locations can be found [here](http://pip.readthedocs.org/en/stable/user_guide/)


## How to build a wheel	

1. Update the version variable in setup.py accordingly.
2. See also the test.bat or test.sh file in your repo.
3. Then run:

    ````sh
    python setup.py bdist_wheel
    ````

## How to add a wheel to your own devpi index	

```
# Login
$ devpi login <uname> --password <upass>

# Change to your devpi index
$ devpi use https://<uname>:<upass>@devpi.mycompany.com/<uname>/dev/

# Upload your wheel
$ devpi upload <wheel_name>.whl
```

## How to remove a wheel from your personal devpi index	

```
# Login
$ devpi login <uname> --password <upass>

# Change to your devpi index
$ devpi use https://<uname>:<upass>@devpi.mycompany.com/<uname>/dev/

# Remove
$ devpi remove <wheel_name_with_or_without_version>
```

## How to remove a wheel from a non-volatile, shared index

(Not recommended. Please try not to create this situation in the first place.)

```
# step 1: ask an admin to help. They will need ssh access to the devpi server
$ ssh admin_name@devpi.mycompany.com

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
```

## How to add a new user

```
$ devpi index <index> acl_upload=<user list>

# E.g. devpi index https://<uname>:<upass>@devpi.mycompany.com/something/master acl_upload=user_a,user_b,user_c
```

## How to add all users to a permission list

```
$ devpi user -l | tr "\\n" "," | xargs -i devpi index mycompany/dev 'acl_upload={}'
```

## How to update user password, email address, title and/or description

```
# First login at the user or root:
$ devpi login <uname> --password 1234
logged in '<uname>', credentials valid for 10.00 hours

# Then modify the desired property:
$ devpi user -m emilie email=<uname>new@gmail.com
/<uname> changing email: <uname>new@gmail.com
user modified: <uname>
```

# How to create user personal index (e.g. <uname>/dev) which should inherit mycompany/dev:

```
devpi login <uname> --password <uname>
devpi index -c dev bases=/mycompany/dev volatile=True

> devpi index https://devpi.mycompany.com/<uname>/dev
https://devpi.mycompany.com/<uname>/dev:
  type=stage
  bases=mycompany/dev
  volatile=True
  uploadtrigger_jenkins=None
  acl_upload=<uname>
  pypi_whitelist=
```
