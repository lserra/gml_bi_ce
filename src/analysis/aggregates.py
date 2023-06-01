#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GMLAggregates:
    def __init__(self, con):
        self.con = con

    def by_cod_nat_juridica(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                nat_juridica AS "nat juridica", 
                count(cnpj) as qty 
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL 
            ORDER BY 2 DESC
            LIMIT 5
            """,
            [uf, municipio, porte],
        ).df()

    def by_municipio(self, uf, porte):
        return self.con.execute(
            """
            SELECT 
                municipio, 
                count(cnpj) as qty 
            FROM bt_empresas 
            WHERE uf = ? 
                AND porte = ? 
            GROUP BY ALL 
            ORDER BY 2 DESC
            LIMIT 5
            """,
            [uf, porte],
        ).df()

    def by_bairro(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                bairro, 
                count(cnpj) as qty 
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL 
            ORDER BY 2 DESC
            LIMIT 5
            """,
            [uf, municipio, porte],
        ).df()

    def by_opc_simples(self, uf, municipio, porte):
        # AVG(DATE_DIFF('day', data_opc_simples::date, data_exc_simples::date)) as avg_duration
        return self.con.execute(
            """
            SELECT 
                opc_simples AS "opc simples", 
                count(cnpj) as qty 
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL 
            ORDER BY 2 DESC
            """,
            [uf, municipio, porte],
        ).df()

    def by_cnae_fiscal(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                cnae_fiscal, 
                count(cnpj) as qty 
            FROM bt_empresas 
            WHERE uf = ? 
                AND municipio = ? 
                AND porte = ? 
            GROUP BY ALL 
            ORDER BY 2 DESC
            LIMIT 5
            """,
            [uf, municipio, porte],
        ).df()
