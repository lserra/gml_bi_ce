#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GMLTables:
    def __init__(self, con):
        self.con = con

    def count_rows(self, uf, municipio, porte):
        return self.con.execute(
            "SELECT COUNT(*) FROM bt_empresas WHERE uf = ? AND municipio = ? AND porte = ?",
            [uf, municipio, porte],
        ).fetchone()[0]

    def list_rows(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT 
                cnpj, 
                matriz_filial AS "matriz filial", 
                razao_social AS "razao social", 
                nome_fantasia AS "nome fantasia", 
                tipo_logradouro AS "tipo logradouro", 
                logradouro, 
                numero, 
                complemento, 
                bairro, 
                cep, 
                ddd_1 AS "ddd1", 
                telefone_1 AS "tel1", 
                ddd_2 AS "ddd2", 
                telefone_2 AS "tel2", 
                email 
            FROM bt_empresas 
            WHERE 
                uf = ? AND 
                municipio = ? AND 
                porte = ? LIMIT 10""",
            [uf, municipio, porte],
        ).df()

    def export_rows(self, uf, municipio, porte):
        return self.con.execute(
            """
            SELECT
                cnpj, 
                matriz_filial, 
                razao_social, 
                nome_fantasia, 
                tipo_logradouro, 
                logradouro, 
                numero, 
                complemento, 
                bairro, 
                cep, 
                ddd_1, 
                telefone_1, 
                ddd_2, 
                telefone_2, 
                email 
            FROM bt_empresas
            WHERE uf = ? AND municipio = ? AND porte = ? 
            """,
            [uf, municipio, porte],
        ).df()
