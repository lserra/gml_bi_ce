#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ==============================================================================
# Copyright (C) 2023 by Data Specialist, Inc. All rights reserved.
# Released under the terms of the GNU General Public License version 2 or later.
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 18/04/2023
# ==============================================================================

# con = duckdb.connect('file.db')
# con.sql('CREATE TABLE integers(i INTEGER)')
# con.sql('INSERT INTO integers VALUES (42)')
# con.sql('SELECT * FROM integers').show()
import duckdb

from config import Config

env = Config()


class GMLDataWarehouseOperations:
    def __init__(self):
        self.db_name = "gmlbi.db"
        self.db_path = f"{env.APP_PATH}/data/output/"
        self.file_path = f"{env.APP_PATH}/data/input/"
        self.db_file = "bt_empresas_db.csv"
        self.table_name = "bt_empresas"

    def connect_db(self):
        try:
            return duckdb.connect(f"{self.db_path}{self.db_name}")

        except duckdb.ConnectionException as error:
            print(f"\n=[ Something went wrong ]=\n{error}")

    def create_table(self):
        try:
            sql = f"""
            CREATE OR REPLACE TABLE {self.table_name} AS
            SELECT *
            FROM read_csv_auto('{self.file_path}{self.db_file}', header=True, delim=';', ignore_errors=True);
            """
            db = self.connect_db()
            db.sql(sql)

        except Exception as error:
            print(f"\n=[ Something went wrong ]=\n{error}")

        finally:
            db.close()

    def execute_query_fetchone(self, sql):
        try:
            db = self.connect_db()
            db.execute(sql)
            return db.sql(sql).fetchone()

        except Exception as error:
            print(f"\n=[ Something went wrong ]=\n{error}")

        finally:
            db.close()

    def execute_query_fetchall(self, sql):
        try:
            db = self.connect_db()
            db.execute(sql)
            return db.sql(sql).fetchall()

        except Exception as error:
            print(f"\n=[ Something went wrong ]=\n{error}")

        finally:
            db.close()

    def execute_query_fetchmany(self, sql):
        try:
            db = self.connect_db()
            db.execute(sql)
            return db.sql(sql).fetchmany()

        except Exception as error:
            print(f"\n=[ Something went wrong ]=\n{error}")

        finally:
            db.close()
