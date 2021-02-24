#!/bin/bash
SHELL=/bin/bash

# bail out if required ENVIRONMENT variables are not given
: ${GATEWAYPORT?"Need to set GATEWAYPORT"}
: ${ROOTDIR?"Need to set ROOTDIR"}


# configure apache site file
sed -i 's@<servername>@'"$SERVERNAME"'@' /etc/apache2/sites-available/process.conf
sed -i 's@<rootdir>@'"$ROOTDIR"'@g' /etc/apache2/sites-available/process.conf

# wsgi config
sed -i 's@sys.path.insert.*$@sys.path.insert(0, '"'$ROOTDIR/myapp/api/platform/app'"')@g' $ROOTDIR/myapp/api/platform/app/wsgi.py
sed -i 's@application.root_path.*$@application.root_path='"'$ROOTDIR/myapp/api/platform/app'"'@g' $ROOTDIR/myapp/api/platform/app/wsgi.py
sed -i 's@application.secret_key.*$@application.secret_key='"'$WSGIKEY'"'@g' $ROOTDIR/myapp/api/platform/app/wsgi.py


PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#chmod -R 777 $DATADIR
nohup apachectl -DFOREGROUND &

cd $ROOTDIR/myapp/api/platform


tail -f /dev/null
