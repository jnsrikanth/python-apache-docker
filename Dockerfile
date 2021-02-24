# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /

RUN apt-get install -y curl iputils-ping 

#######################################
# APACHE SERVER WITH PYTHON MODULE
# this is needed for serving images
#######################################
RUN apt-get update
RUN apt-get install -y apache2 libapache2-mod-wsgi-py3 &&\
    dpkg -S mod_wsgi
#RUN libapache2-mod-security2 pkg-config &&\
    
#######################################
# APACHE SETUP
#######################################

RUN mkdir /etc/apache2/log &&\
    mkdir /etc/apache2/log/process
    
COPY ./process.conf /etc/apache2/sites-available/

RUN a2enmod ssl &&\
    a2enmod headers &&\
    a2ensite process.conf

#######################################
# NETWORKING & MONITORING
#######################################
RUN apt-get update &&\
    apt-get install -y openssh-server &&\
    mkdir /var/run/sshd &&\
    chmod 0755 /var/run/sshd &&\
    useradd --create-home --shell /bin/bash --groups sudo appadmin

RUN apt-get -y upgrade &&\
    apt-get install -y patch &&\
    apt-get dist-upgrade &&\
    apt-get autoremove

ARG ROOTDIR=/home/cpxroot

WORKDIR /

RUN mkdir -p $ROOTDIR/myapp/api/platform &&\
    mkdir -p $ROOTDIR/myapp/api/platform/app &&\
    mkdir -p $ROOTDIR/myapp/api/error_logs/process_api &&\
    mkdir -p $ROOTDIR/myapp/api/error_logs/agent_api


RUN mkdir $ROOTDIR/certs
COPY ./certs/default.crt $ROOTDIR/certs
COPY ./certs/default.key $ROOTDIR/certs


WORKDIR $ROOTDIR/myapp/api/platform
# copy the content of the local directory to the working directory
COPY . $ROOTDIR/myapp/api/platform/app

WORKDIR $ROOTDIR/myapp/api/platform/app
# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

#######################################
# STARTUP COMMAND
#######################################
COPY ./startup.sh $ROOTDIR/myapp/api/platform/app
RUN chmod 755 $ROOTDIR/myapp/api/platform/app/startup.sh

WORKDIR $ROOTDIR/myapp/api/platform/app
CMD ["./startup.sh"]
