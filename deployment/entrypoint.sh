#!/bin/bash

apt-get update

apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 wget gnupg apt-utils

curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

apt-get -y update

apt-get -y install google-chrome-stable

wget https://chromedriver.storage.googleapis.com/103.0.5060.53/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

mv chromedriver /usr/bin/chromedriver

chown root:root /usr/bin/chromedriver

chmod +x /usr/bin/chromedriver