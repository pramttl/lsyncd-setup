'''
Script that interactively creates an lsync config file.
Notes:

* The same target path is assumed for all the slaves although IP can be different.
* Run this script as a root.
'''

import os

print "Enter source dir path (Example: /home/master/source/)"
source_path = raw_input()

print "Enter comma separated list of slave ip's"
str_slaves = raw_input()
slaves = str_slaves.split(',')

print "Enter destination dir path (Example: /home/slave/dest/)"
dest_path = raw_input()

str_config = '''
settings {
    logfile = "/var/log/lsyncd/lsyncd.log",
    statusFile = "/var/log/lsyncd/lsyncd-status.log",
    statusInterval = 20
}

sync {
  default.rsync,
  source="%(source_path)s",
'''% { 'source_path': source_path }

for slave in slaves:
    str_config += 'target='+ slave + ':/home/ubuntu/temp/syncedup/",\n'

str_config += '''
  rsync = {
    compress = true,
    acls = true,
    verbose = true,
    rsh = "/usr/bin/ssh -p 22 -o StrictHostKeyChecking=no" }
}
'''

try:
    f = open('/etc/lsyncd.lua', 'w')
    f.write(str_config)
    f.close()

    print "----------------------------------------------------------------"
    print "The following lsyncd config has been written to: /etc/lsyncd.lua"
    print "----------------------------------------------------------------"
    print str_config

except:
    print "You need to run this script as a root or with superuser permissions for saving conig"
    print "You can manually save the following file at: /etc/lsyncd.lua"
    print str_config
