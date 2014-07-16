#DOCKER-VERSION 0.3.4
FROM        ubuntu:14.04
RUN         apt-get update
RUN         apt-get -y install curl g++ make
RUN         apt-get -y install git python-protobuf python-dev
RUN         export LD_LIBRARY_PATH=/usr/local/lib
RUN         cd /home && curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN         pip install -U six==1.7.3
RUN         pip install -U pyramid==1.5.1
RUN         pip install -U pyramid_contextauth==0.7.2
RUN         pip install -U pyramid_webassets==0.7.1
RUN         pip install -U pyramid_fanstatic==0.5
RUN         pip install -U waitress==0.8.9
RUN         pip install -U SQLAlchemy==0.9.6
RUN         pip install -U pyramid_tm==0.7
RUN         pip install -U zope.sqlalchemy==0.7.5
RUN         pip install -U pyramid_jinja2==2.3.2
WORKDIR     /home
RUN         pcreate -s starter MyProject
WORKDIR     /home/MyProject
RUN         python setup.py develop
WORKDIR     /home
RUN         pip install -U fabric==1.9.0
RUN         apt-get install -y libyaml-dev
RUN         pip install -U PyYAML==3.11
RUN         pip install -U cython==0.20.2
RUN         pip install -U sass==2.2
RUN         apt-get install -y ruby
RUN         gem install sass
