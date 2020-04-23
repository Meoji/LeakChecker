#!/bin/python
import hashlib
import requests
import getpass
import os

red = '\033[38;2;255;0;0m\033m'
orange = '\033[38;2;255;190;115m\033m'
yellow = '\033[38;2;200;200;115m\033m'
white = '\033[38;2;255;255;255m\033m'
print (orange)
os.system('clear')

hash=hashlib.sha1(getpass.getpass().encode("utf-8")).hexdigest().upper()
head,tail = hash[:5],hash[5:]
url='https://api.pwnedpasswords.com/range/'+head
res=requests.get(url)

if not res.ok:
        raise RuntimeError('Failed to fetch "{}": "{}"'.format(url. res.status_code))

hs=(line.split(':') for line in res.text.splitlines())
count=next((int(count) for t,count in hs if t==tail),0)
print("")
print(yellow + "Hash: " + hash)
print (red)
print("Your password has been compromised ", count, "times")
print (white)
