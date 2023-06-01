#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GMLMetrics:
    def __init__(self, con):
        self.con = con

    def get_value_total_empresas(self, uf, municipio, porte):
        sql = f"SELECT COUNT(*) FROM bt_empresas WHERE uf = '{uf}' AND municipio = '{municipio}' AND porte = '{porte}'"
        return self.con.execute(sql).fetchone()[0] if not None else 0

    def get_value_total_empresas_publica(self, uf, municipio, porte):
        sql = (
            f"SELECT COUNT(*) FROM bt_empresas WHERE cod_nat_juridica IN ('2305', '2313') AND uf = '{uf}' "
            f"AND municipio = '{municipio}' AND porte = '{porte}'"
        )
        return self.con.execute(sql).fetchone()[0] if not None else 0

    def get_value_total_empresas_individual(self, uf, municipio, porte):
        sql = (
            f"SELECT COUNT(*) FROM bt_empresas WHERE cod_nat_juridica IN ('2305', '2313') AND uf = '{uf}' "
            f"AND municipio = '{municipio}' AND porte = '{porte}'"
        )
        return self.con.execute(sql).fetchone()[0] if not None else 0

    def get_value_total_empresas_sociedade_anonima(self, uf, municipio, porte):
        sql = (
            f"SELECT COUNT(*) FROM bt_empresas WHERE cod_nat_juridica IN ('2046', '2054') AND uf = '{uf}' "
            f"AND municipio = '{municipio}' AND porte = '{porte}'"
        )
        return self.con.execute(sql).fetchone()[0] if not None else 0

    def get_value_total_empresas_sociedade_limitada(self, uf, municipio, porte):
        sql = (
            f"SELECT COUNT(*) FROM bt_empresas WHERE cod_nat_juridica = '2062' AND uf = '{uf}' "
            f"AND municipio = '{municipio}' AND porte = '{porte}'"
        )
        return self.con.execute(sql).fetchone()[0] if not None else 0
