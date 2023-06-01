#!/bin/bash

# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 25/04/2023
# ======================================================================================
export TERM=xterm
cd $APP_PATH || exit

clear

echo
echo "=========================== [ GML BI TOOLS ] ====================================="
echo "=================================================================================="
echo "[                         CHECKING APPLICATION . . .                             ]"
echo "=================================================================================="
echo

dir="./data"
if [ -d $dir ]; then
  echo "===> [OK] - '/data' directory found!"
else
  echo "===> [NOK] - '/data' directory NOT found!"
	exit
fi

dir="./logs"
if [ -d $dir ]; then
  echo "===> [OK] - '/logs' directory found!"
else
  echo "===> [NOK] - '/logs' directory NOT found!"
	exit
fi

dir="./src"
if [ -d $dir ]; then
  echo "===> [OK] - '/src' directory found!"
else
  echo "===> [NOK] - '/src' directory NOT found!"
	exit
fi

# Check for file existence
file="./src/extract/get_file_from_gold_layer.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: get_file_from_gold_layer.py found"
else
	echo "===> [NOK] - SCRIPT: get_file_from_gold_layer.py NOT found!"
	exit
fi

file="./src/load/put_bt_empresas_in_dw.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: put_bt_empresas_in_dw.py found"
else
	echo "===> [NOK] - SCRIPT: put_bt_empresas_in_dw.py NOT found!"
	exit
fi

file="./src/utils/dl_operations.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: dl_operations.py found"
else
	echo "===> [NOK] - SCRIPT: dl_operations.py NOT found!"
	exit
fi

file="./src/utils/dw_operations.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: dw_operations.py found"
else
	echo "===> [NOK] - SCRIPT: dw_operations.py NOT found!"
	exit
fi

file="./src/utils/logger_app.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: logger_app.py found"
else
	echo "===> [NOK] - SCRIPT: logger_app.py NOT found!"
	exit
fi

file="wat.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: wat.py found"
else
	echo "===> [NOK] - SCRIPT: wat.py NOT found!"
	exit
fi

file="config.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: config.py found"
else
	echo "===> [NOK] - SCRIPT: config.py NOT found!"
	exit
fi

file="dashboard.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: dashboard.py found"
else
	echo "===> [NOK] - SCRIPT: dashboard.py NOT found!"
	exit
fi

file="login.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: login.py found"
else
	echo "===> [NOK] - SCRIPT: login.py NOT found!"
	exit
fi

file="test_gml_bi.py"
if [ -e $file ]; then
	echo "===> [OK] - SCRIPT: test_gml_bi.py found"
else
	echo "===> [NOK] - SCRIPT: test_gml_bi.py NOT found!"
	exit
fi

echo
echo "=================================================================================="
echo "[                           RUNNING TESTS . . .                                  ]"
echo "=================================================================================="
echo

# Check if file is readable/executable
file="test_gml_bi.py"
if [ -r $file ]; then
  python3 $file
else
  echo "===> [NOK] - SCRIPT: 'test_gml_bi.py' is NOT readable!"
  exit
fi

echo
echo "=================================================================================="
echo "[                           RUNNING JOBS . . .                                   ]"
echo "=================================================================================="
echo

# Check if file is readable/executable
file="wat.py"
if [ -r $file ]; then
  python3 $file
else
  echo "===> [NOK] - SCRIPT: 'wat.py' is NOT readable!"
  exit
fi

echo
echo "=================================================================================="
echo "[                           JOBS FINISHED . . .                                  ]"
echo "=================================================================================="
echo

file="login.py"
if [ -r $file ]; then
  streamlit run $file --server.port=8501 --server.address=0.0.0.0
else
  echo "===> [NOK] - SCRIPT: 'dashboard.py' is NOT readable!"
  exit
fi
