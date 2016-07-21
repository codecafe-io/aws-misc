#!/usr/bin/env bash

SCRIPT_NAME=$(basename "$0")
export LOG_FILE="/var/log/$SCRIPT_NAME.log"
exec 6>&1 7>&2 &>$LOG_FILE
echo "Starting $SCRIPT_NAME"

if [ -z $BASE_FOLDER ]; then
                export BASE_FOLDER="application/monitoring";
fi

echo "BASE_FOLDER=$BASE_FOLDER"

AWS_REGION=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone/ | cut -c 1-9`
LOCAL_IP=`/usr/bin/curl -s http://169.254.169.254/latest/meta-data/local-ipv4`

echo $AWS_REGION
echo $LOCAL_IP

echo " Done "
exec 1>&6 2>&7 6>&- 7>&-
