#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ======================================================================================
# Copyright (C) 2023 by Data Specialist, Inc. All rights reserved.
# Released under the terms of the GNU General Public License version 2 or later.
# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 28/04/2023
# ======================================================================================
# WAT: WEB ANALYSIS TOOL
# ======================================================================================
import typer

import eda_tool

app = typer.Typer(name="gml-bi", add_completion=False, help="GML-BI Application")


@app.command()
def main(uf: str):
    """Starts GML-BI Application"""
    eda_tool.start(str.upper(uf))


if __name__ == "__main__":
    app()
