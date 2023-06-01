#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.utils.dw_operations import GMLDataWarehouseOperations


class TestGmlBIOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.dw = GMLDataWarehouseOperations()

    def test_db_connect(self):
        """Testing DuckDB connection"""
        db = self.dw.connect_db()
        self.assertEqual(db is not None, True, "Database connection failed . . .")

    def test_table_exists(self):
        """Testing bt_empresas is available"""
        sql = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='bt_empresas';"
        count = self.dw.execute_query_fetchone(sql)[0]
        self.assertEqual(count, 1, "Table is not available . . .")

    def test_total_columns_in_table(self):
        """Testing total of columns"""
        sql = "PRAGMA table_info('bt_empresas');"
        columns = self.dw.execute_query_fetchall(sql)
        self.assertEqual(len(columns), 44, "Columns not matching . . .")

    def test_total_rows_in_table(self):
        """Testing total of rows"""
        sql = "SELECT COUNT(*) FROM bt_empresas;"
        rows = self.dw.execute_query_fetchone(sql)[0]
        self.assertEqual(rows >= 6331292, True, "Rows not matching . . .")


if __name__ == "__main__":
    unittest.main()
