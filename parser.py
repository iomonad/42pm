#!/usr/bin/python

import json

with open('config.json', 'r') as f:
    conf = json.load(f) 
print json.dumps(conf, indent=4, sort_keys=True)

files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ] #list comprehension version.
with open('./Makefile') as infile, open('tmp', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)
