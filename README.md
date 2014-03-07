## Setting up Lsyncd on a master/slave architecture.

### Problem definition

We want to be able push changes to a directory on the master to the slaves.
In other words, we need to sync the master source with the slave(s) destination.

* One master with a source directory.

  <master-ip>:/path/to/source


* Multiple slave machines where we want to sync the above directory.

  <slave-i>:/path/to/dest

By sync, we mean that any changes to file in source should be reflected in the
destination.



### Push based sync up model using lsyncd

One model for syncing up destinations from the source would be to periodically
check for content at the source. Some ideas involve using a target file on the 
master that is written after files that are to be synced up are changed.

The other model that we are going to test with this code is the push based model
which makes use of `lsyncd`


### Setup

#### Step-1: Public ssh key of master added to all slaves

Ensure master can ssh into slaves from the same user that lsyncd is setup to use.
Make sure the master public key is added to the .ssh directory in all the slaves
and also added to the authorized_keys.


#### Step 2: (On Master) Installing lsync dependencies

  apt-get update && apt-get install -y lua5.1 liblua5.1-dev pkg-config rsync asciidoc make


#### Step 3: (On Master) Install lsyncd

    wget http://lsyncd.googlecode.com/files/lsyncd-2.1.5.tar.gz
    tar xzvf lsyncd-2.1.5.tar.gz
    cd lsyncd-2.1.5
    ./configure && make && make install

Now lsyncd service is installed on the master. The configuration scripts still
need to be setup. Also lsyncd doesn't start itself so we need to start it explicitly ahead.

#### Step 4: (Optional) Startup scripts

This step is optional if you are experienced. Its convenient to have startup scripts
which will make it easy ahead to start lsyncd.

        # sudo python init-lsyncd.py


#### Step 5: Create lsyncd configuration

This repository provies a python file that you can run interactively to generate
the lsyncd configuration file. It also places the configuration file at the required
location if you run the code as a superuser.

        # python interactive-gen-config.py


#### Step 6: start lsyncd

        start lsyncd


### Credits:

Thanks to rackspace for an excellent [tutorial](http://www.rackspace.com/knowledge_center/article/install-and-configure-lsyncd)
