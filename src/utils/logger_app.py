#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================================
# Copyright (C) 2023 by Data Specialist, Inc. All rights reserved.
# Released under the terms of the GNU General Public License version 2 or later.
# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 03/03/2023
# ======================================================================================
import logging
import logging.handlers

from config import Config

env = Config()


class LoggerApp:
    def __init__(self, filename):
        self.app_name = env.APP_NAME
        self.log_path = f"{env.APP_PATH}/logs/"
        self.log_filename = f"{filename}.log"

    def logging_application(self):
        # Logger initialization
        logger = logging.getLogger(self.app_name)
        logger.setLevel(logging.DEBUG)

        # Creating file log handler and set level to debug
        ch = logging.FileHandler(f"{self.log_path}{self.log_filename}", "w+")
        ch.setLevel(logging.DEBUG)

        # Creating formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Adding formatter to ch
        ch.setFormatter(formatter)

        # Adding ch to logger
        logger.addHandler(ch)

        # Setting the Logger Level (INFO)
        logger.setLevel(logging.INFO)

        return logger
