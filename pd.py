import sys, os
ref, host, command = [line.rstrip('\n') for line in open('ref_pkgs.txt', 'r')], [line.rstrip('\n') for line in open('host_pkgs.txt', 'r')], "pakku -S"
for x in (r for r in ref if r not in host): command += " " + x
if input('\n' + command + '\n\nAre you sure you would like to run the above command?\nYou will be installing ' + str(len(ref) - len(host)) + ' packages. [y/n]: ').lower() == 'y': os.system(command)