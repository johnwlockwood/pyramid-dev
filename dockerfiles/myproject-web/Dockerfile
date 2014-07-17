#DOCKER-VERSION 0.3.4
FROM        johnwlockwood/db-client-base
RUN         rm -R /home/MyProject
RUN         rm /usr/local/lib/python2.7/dist-packages/MyProject.egg-link
ADD         ./MyProject.egg-link /usr/local/lib/python2.7/dist-packages/
