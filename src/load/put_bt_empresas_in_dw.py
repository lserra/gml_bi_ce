#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ==============================================================================
# Copyright (C) 2023 by Data Specialist, Inc. All rights reserved.
# Released under the terms of the GNU General Public License version 2 or later.
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 18/04/2023
# ==============================================================================
import os

from config import Config
from src.utils.dw_operations import GMLDataWarehouseOperations
from src.utils.logger_app import LoggerApp

env = Config()


def delete_data(local_path):
    """Delete old data in the local path"""
    files = os.listdir(local_path)
    for file in files:
        os.remove(f"{local_path}{file}")
        print(f"-----> File {file} have been deleted from {local_path}")


def load_data(local_path):
    """Load file(s) from the local path to DuckDB (DW)"""
    logger = LoggerApp(filename="loading-data-gold-layer").logging_application()
    logger.info("======================= START =======================")
    logger.info(f"Getting data from the local folder: {local_path}")
    try:
        dw = GMLDataWarehouseOperations()
        dw.create_table()
        res = dw.execute_query_fetchone("SELECT count(*) FROM bt_empresas;")

        logger.info(f"Total of {res[0]} rows have been loaded")
        logger.info("=======================  END  =======================")

        return res[0]

    except Exception as error:
        print(f"\n=[ Something went wrong ]=\n{error}")
    finally:
        logger.handlers[0].stream.close()
        logger.removeHandler(logger.handlers[0])


def run():
    input_path = f"{env.APP_PATH}/data/input/"
    output_path = f"{env.APP_PATH}/data/output/"
    delete_data(local_path=output_path)
    total_rows = load_data(local_path=input_path)
    if total_rows > 0:
        print(f"\n-----> Process finished successfully!")
