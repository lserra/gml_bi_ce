#!/bin/bash

# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 25/04/2023
# ======================================================================================
ENV=$1

export TERM=xterm
cd $APP_PATH || exit

clear

echo
echo "=========================== [ GML BI TOOLS ] ====================================="
echo "=================================================================================="
echo "[             W E L C O M E   T O   G M L   B I   T O O L S                      ]"
echo "=================================================================================="
echo
echo "SETTINGS:"
echo "> Working dir:" $PWD
echo "> Environment:" $ENV
echo
echo "STARTING APPLICATION . . ."

case $ENV in
"dev")
  /bin/bash ./start_app_dev.sh;;
"test")
  /bin/bash ./start_app_test.sh;;
"prod")
  /bin/bash ./start_app_prod.sh;;
"terminal")
  /bin/bash;;
esac
exit
