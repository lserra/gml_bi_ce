#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GMLQueries:
    def __init__(self, con):
        self.con = con

    def get_rows_uf_filtered(self, uf):
        return self.con.execute(
            """
            SELECT * 
            FROM bt_empresas 
            WHERE uf = ? 
            """,
            [uf],
        ).df()
