#!/bin/bash

git checkout master
git pull origin master
systemctl restart apache2
