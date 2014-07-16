# Pyramid Dev with Docker - Database and Asset Managment starter 

The following instructions are a little tuned to Mac OS X, if you're running linux you can skip the Vagrant stuff
and just run docker.

## Development

### Setup the for first time

* Install [Vagrant](http://www.vagrantup.com)
* clone [pyramid-docker repo](https://github.com/johnwlockwood/pyramid-docker) and run `vagrant up` from there
* clone this repo into pyramid-docker
* connect to vagrant with `vagrant ssh`
* cd /vagrant/pyramid-dev

#### Build the docker images

Building the images only have to be done once, except later if there are more instructions added to the DockerFiles, at that time, the images can be updated.

at `vagrant@ubuntu-14:~$ `

    docker build -t johnwlockwood/pyramid-base dockerfiles/pyramid-base/

Wait for it to finish, then build the development image:

at `vagrant@ubuntu-14:~$ `

    docker build -t johnwlockwood/db-client-base dockerfiles/db-client-base/
    docker build -t johnwlockwood/myproject-web dockerfiles/myproject-web/


#### Initialize the database container
The web application will connect to the database, so the database needs to be setup first.
Today, we will use MySQL.

at `vagrant@ubuntu-14:~$ `

    docker run --name db_mysql -e MYSQL_ROOT_PASSWORD=mysecretpassword -d mysql
    
The mysql image will be installed and run as the container named `db_mysql`

#### Setup this project for development

at `vagrant@ubuntu-14:~$ `

    docker run --rm -v /vagrant:/workspace --workdir="/workspace/pyramid-dev/MyProject" johnwlockwood/myproject-web sh -c "python setup.py develop"

#### Create and run the development webserver named `devweb1`

Run the development config of the server with auto-reload on changes:

    docker run --name devweb1 -v /vagrant:/workspace --link nl_mysql:mysql -p 6543:6543 -P -d --workdir="/workspace/pyramid-dev/MyProject" johnwlockwood/myproject-web pserve development.ini --reload

### Access webserver from your computer.

With your browser, access the [development site] (http://localhost:6543/). You can access it from any computer on your network using your host computer's IP address instead of localhost.

## Do development on the site

From another terminal on your computer cd into the pyramid-dev directory and you can run git commands on this project such as pulling down the latest changes to a branch or making your own branch to work on. Doing it this way let's you use your github ssh key already setup and keeps it off the virtual machine.
Edit the files in MyProject such as one of the template files in `MyProject/myproject/templates` or one of the css files such as `MyProject/myproject/static/assets/css/theme.css` and then when you refresh the browser you will see the changes.


MyProject is a [pyramid](http://docs.pylonsproject.org/projects/pyramid/en/1.5-branch/narr/project.html) project

[Webassets](http://webassets.readthedocs.org/en/latest/bundles.html) is installed and a sample bundle is defined in `MyProject/myproject/__init__.py` It compiles a few different css and SASS files into one css file or in debug mode, it just compiles the SASS file into a css file when changes are made to it.


## New to vagrant?

Once you cd into the pyramid-docker you can run vagrant commands to control the 
virtual machine.

### Check status of the virtual machine

Check it's status, it may aready be running if you had started it previously:

    pyramid-docker $ vagrant status
    Current machine states:

    default                   saved (virtualbox)

    To resume this VM, simply run `vagrant up`.

### Start up the virtual machine

If it's not saved or not running, you will do `vagrant up` to start or resume it.
then do `vagrant status` again:

    pyramid-docker $ vagrant status
    Current machine states:

    default                   running (virtualbox)

    The VM is running. To stop this VM, you can run `vagrant halt` to
    shut it down forcefully, or you can run `vagrant suspend` to simply
    suspend the virtual machine. In either case, to restart it again,
    simply run `vagrant up`.

It describes how to stop the VM and restart it.
Before you turn off your computer it's best to suspend the virtual machine so when it is resumed,
it still has everything running as before.

### Connect to the virtual machine

Once it's running, then you can connect to it via ssh:

    pyramid-docker $ vagrant ssh
    Welcome to Ubuntu 14.04 LTS (GNU/Linux 3.13.0-24-generic x86_64)

     * Documentation:  https://help.ubuntu.com/
    Last login: Sat Jul 12 05:44:55 2014 from 10.0.2.2
    vagrant@ubuntu-14:~$

### Run some docker commands
#### See running containers
This puts you at the virtual machine's command prompt. From here you can run docker commands.
I since I had suspended the VM from before, when I check the running docker containers with
the `docker ps` command, it shows the `devweb1` container is running:

    vagrant@ubuntu-14:~$ docker ps
    CONTAINER ID        IMAGE                               COMMAND                CREATED             STATUS              PORTS                    NAMES
    142b95084ce1        johnwlockwood/myproject-web:latest   pserve development.i   3 days ago          Up 39 hours         0.0.0.0:6543->6543/tcp   devweb1

#### Stop a running container

If it is running, you can try stopping it by name

at `vagrant@ubuntu-14:~$ `

    docker stop devweb1

If there is no container running, you won't see anything below the headers.

    vagrant@ubuntu-14:~$ docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

If you previously ran the commands above that start with `docker run`, you may
just need to start it.

#### See all of your existing docker containers

    vagrant@ubuntu-14:~$ docker ps -a
    CONTAINER ID        IMAGE                               COMMAND                CREATED             STATUS                    PORTS                    NAMES
    142b95084ce1        johnwlockwood/myproject-web:latest   pserve development.i   3 days ago          Up 40 hours               0.0.0.0:6543->6543/tcp   devweb1

#### Start the stopped webserver

The webserver container is named `devweb1`, start it with the docker start command:

    vagrant@ubuntu-14:~$ docker start devweb1

### Browse the site

At this point I can go to the web browser on my computer and browse to http://localhost:6543.

### Exit and Save at the end of the day

If you are in the VM, you see the `vagrant@ubuntu-14:~$` prompt, then you can exit the VM with `exit`.
it will remain running and you can `vagrant ssh` back into it a will.

### Extra (optional)

#### Start and connect to the shell on project image 

Run a container interactively to initialize the volume /workspace:

    vagrant@ubuntu-14:~$ docker run --rm -v /vagrant:/workspace --link nl_mysql:mysql -t -i -P --workdir="/workspace/pyramid-dev/MyProject" johnwlockwood/myproject-web /bin/bash
    root@cc77be734ced:/workspace/pyramid-dev/MyProject#

#### Exit the container

Exiting the container will bring you back to the vagrant command prompt:

    root@cc77be734ced:/workspace/pyramid-dev/MyProject# exit
    exit
    vagrant@ubuntu-14:~$

