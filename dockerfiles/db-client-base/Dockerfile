#DOCKER-VERSION 0.3.4
FROM        johnwlockwood/pyramid-base
RUN         apt-get install -y libmysqlclient-dev
RUN         pip install -U MySQL-python==1.2.5
RUN         apt-get install -y unixodbc-dev
RUN         apt-get install -y unzip
WORKDIR     /home
RUN         curl -O https://pyodbc.googlecode.com/files/pyodbc-3.0.7.zip
RUN         unzip pyodbc-3.0.7.zip
WORKDIR     /home/pyodbc-3.0.7
RUN         python setup.py build
RUN         python setup.py install
