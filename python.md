# Python

```
################################################################################
# Failed to create virtualenv?

virtualenv -p python2.7 --no-site-packages --no-download  env_27

################################################################################
# How to fix ImportMismatchError in Python

find . -name \*.pyc -delete

################################################################################
# Download tar.gz from pypi without md5 code

wget --recursive --no-directories --accept=Rtree-0.8.3.tar.gz https://pypi.python.org/simple/rtree/

# OR (--no-binary)

pip download --no-deps -d ./some_source -i https://pypi.python.org/simple --no-binary :all: rtree=="${VERSION}"

================================================================================
# Building a wheel

pip wheel psycopg2==2.6.1 -i https://pypi.python.org/pypi

################################################################################
# pip install --find-links

pip install --find-links <path-to>/dist -e .
pip install --find-links <path-to>/dist -r requirements.txt

################################################################################
# pip: pipdeptree

pip install -r requirements.txt    (for whatever library you want to know about)
pip install pipdeptree
pipdeptree --freeze

################################################################################
# Python debugger

import ipdb; ipdb.set_trace()

################################################################################
# pip force re-install

pip install --force-reinstall --ignore-installed boto3

################################################################################
# Install pip

sudo apt-get remove python-pip python-setuptools
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

################################################################################
# bcrypt

import bcrypt
bcrypt.hashpw('this_is_not_a_pass', bcrypt.gensalt())
'$2a$12$ErFw7xv65Tbp6JOwoQQsCeumpVXfxkoVWLw9wEAqXbhf9Sx9yf6d.'
'$2a$12$IWegt7R.TzQBDRqi0G0mDOXyGBSzjYW4l32Xp85aQI7u9W452n072'

```