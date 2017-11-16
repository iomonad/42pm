#!/usr/bin/python

import json
import os

with open('config.json', 'r') as f:
    conf = json.load(f) 
files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ] 
with open('./Makefile') as infile, open('tmp', 'w') as outfile:
    for line in infile:
        for src, target in conf.iteritems():
            line = line.replace(src, target)
        outfile.write(line)
