#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GMLFilters:
    def __init__(self, con):
        self.con = con

    def by_uf(self):
        return self.con.execute("SELECT DISTINCT uf FROM bt_empresas ORDER BY uf").df()

    def by_municipio(self, uf):
        return self.con.execute(
            "SELECT DISTINCT municipio FROM bt_empresas WHERE uf = ? ORDER BY municipio ASC",
            [uf],
        ).df()

    def by_porte(self, uf, municipio):
        return self.con.execute(
            "SELECT porte FROM bt_empresas WHERE uf = ? AND municipio = ?",
            [uf, municipio],
        ).fetchone()
