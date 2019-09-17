import sys, os

ref = [line.rstrip('\n') for line in open('ref_pkgs.txt', 'r')]

host = [line.rstrip('\n') for line in open('host_pkgs.txt', 'r')]

command = "pakku -S"

for r in ref:
	if r not in host:
		command += " " + r

print(command)