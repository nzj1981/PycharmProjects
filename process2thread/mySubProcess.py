#!/usr/bin/env python3
# coding=utf-8

import subprocess

print('$ nslookup www.echargenet.com')

r = subprocess.call(['nslookup', 'www.echargenet.com'])

print('Exit code:', r)
