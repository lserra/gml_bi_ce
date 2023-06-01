#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GMLCharts:
    def __init__(self, con):
        self.con = con

    def by_opc_mei(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                opc_mei AS "opc mei", 
                count(cnpj) AS qty
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL
            """,
            [uf, municipio, porte],
        ).df()

    def by_matriz_filial(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                matriz_filial AS "matriz filial", 
                count(cnpj) AS qty
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL
            """,
            [uf, municipio, porte],
        ).df()

    def by_situacao(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                situacao, 
                count(cnpj) AS qty
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL
            """,
            [uf, municipio, porte],
        ).df()
