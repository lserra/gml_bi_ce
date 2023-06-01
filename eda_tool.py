#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ======================================================================================
# Copyright (C) 2023 by Data Specialist, Inc. All rights reserved.
# Released under the terms of the GNU General Public License version 2 or later.
# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 28/04/2023
# ======================================================================================
# EDA: EXPLORATORY DATA ANALYSIS TOOL (USING D-TALE)
# ======================================================================================
import dtale

from src.analysis.queries import GMLQueries
from src.utils.dw_operations import GMLDataWarehouseOperations


def start(uf: str):
    dw = GMLDataWarehouseOperations()
    con = dw.connect_db()

    qry = GMLQueries(con)
    df = qry.get_rows_uf_filtered(uf)

    dtale.show(df, subprocess=False)
