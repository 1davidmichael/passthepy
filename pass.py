#!/usr/bin/env python

import gnupg
import argparse
import os.path
import xerox
import logging

logging.basicConfig(level=logging.DEBUG)

gnupg_home = os.path.expanduser("~") + "/.gnupg"
pass_home = os.path.expanduser("~") + "/.password-store"
gpg = gnupg.GPG(gnupghome=gnupg_home)

fp = open(pass_home + "/Work/ultradns.gpg")

print gpg.decrypt_file(fp)

print gnupg_home


