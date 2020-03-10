#!/bin/bash

user=monitoring
python=`which python3`
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
MAIN="$SCRIPTPATH/main.py"

LOG_DIR=/var/log/monitoring

runuser -l $user -c "$python $MAIN 2>>$LOG_DIR/error.log" 
