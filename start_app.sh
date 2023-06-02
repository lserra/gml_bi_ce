#!/bin/bash

# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 25/04/2023
# ======================================================================================
TOOL=$1

export TERM=xterm

clear

echo
echo "=========================== [ GML BI TOOLS ] ====================================="
echo "=================================================================================="
echo "[             W E L C O M E   T O   G M L   B I   T O O L S                      ]"
echo "=================================================================================="
echo
echo "SETTINGS:"
echo "> Working dir:" $PWD
echo "> BI Tool:" $TOOL
echo

case $TOOL in
"dash")
  /bin/bash $PWD/start_bi_app.sh;;
"eda")
  /bin/bash $PWD/start_eda_app.sh;;
"terminal")
  /bin/bash;;
esac
exit
