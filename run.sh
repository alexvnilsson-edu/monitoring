#!/bin/bash

python=`which python3`
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
MAIN="$SCRIPTPATH/main.py"

LOG_DIR=/var/log/monitoring

$python $MAIN 1>>$LOG_DIR/monitoring.log 2>>$LOG_DIR/error.log
