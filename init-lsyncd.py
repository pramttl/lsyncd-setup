import os

# Create  the init config string.
init_path = '/etc/init/lsyncd.conf'
str_conf = '''
description "lsyncd file syncronizer"
    
    start on (starting network-interface
        or starting network-manager
        or starting networking)
                
        stop on runlevel [!2345]
        
        expect fork
        
        respawn
        respawn limit 10 5
               
        exec /usr/local/bin/lsyncd /etc/lsyncd.lua
'''
f = open(init_path, 'w')
f.write(str_conf)
f.close()


# Create lsyncd symlink that starts upstart-job
os.system('ln -s /lib/init/upstart-job /etc/init.d/lsyncd')
