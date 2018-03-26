#/bin/bash

# install pyinstaller
pip install --trusted-host \
	pypi.douban.com pyinstaller \
	-i http://pypi.douban.com/simple
git config --global user.email "gzmanyang@gmail.com"
git config --global user.name "manyang901"
git config --global credential.helper store