#!/bin/bash

# adds some useful aliases
# Author: Neal Brophy

# django
echo "alias pymanage='python3 manage.py'" >> ~/.bashrc
echo "alias runs='python3 manage.py runserver'" >> ~/.bashrc
echo "alias startp='django-admin startproject'" >> ~/.bashrc
echo "alias starta='python3 manage.py startapp'" >> ~/.bashrc
echo "alias maked='python3 manage.py makemigrations --dry-run'" >> ~/.bashrc
echo "alias makem='python3 manage.py makemigrations'" >> ~/.bashrc
echo "alias planmig='python3 manage.py migrate --plan'" >> ~/.bashrc
echo "alias showmig='python3 manage.py showmigrations'" >> ~/.bashrc
echo "alias migrate='python3 manage.py migrate'" >> ~/.bashrc
echo "alias createsu='python3 manage.py createsuperuser'" >> ~/.bashrc

# git
echo "alias gstatus='git status'" >> ~/.bashrc
echo "alias gadd='git add'" >> ~/.bashrc
echo "alias gcommit='git commit -m'" >> ~/.bashrc
echo "alias grevert='git revert'" >> ~/.bashrc
echo "Done"
source ~/.bashrc