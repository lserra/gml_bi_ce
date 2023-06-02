#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ======================================================================================
# Copyright (C) 2023 by Data Specialist, Inc. All rights reserved.
# Released under the terms of the GNU General Public License version 2 or later.
# ======================================================================================
# Created by: laercio.serra@gmail.com
# Created at: 30/05/2023
# ======================================================================================
# DASH: DASHBOARD TOOL (USING STREAMLIT)
# ======================================================================================
from timeit import default_timer as timer

import streamlit as st

from config import Config
from src.analysis.aggregates import GMLAggregates
from src.analysis.charts import GMLCharts
from src.analysis.filters import GMLFilters
from src.analysis.metrics import GMLMetrics
from src.analysis.tables import GMLTables
from src.utils.dw_operations import GMLDataWarehouseOperations

# Initializing objects
env = Config()

dw = GMLDataWarehouseOperations()
con = dw.connect_db()

agg = GMLAggregates(con)
chart = GMLCharts(con)
filter = GMLFilters(con)
metric = GMLMetrics(con)
table = GMLTables(con)

# Initializing variables
uf = ""
municipio = ""
porte = ""
start_timer = ""
end_timer = ""


def page_header():
    # st.set_page_config(layout="wide")
    st.title("Get More Leads (CNPJ)")
    with st.expander("About the data"):
        st.write(env.APP_FULL_DESC)


def page_footer(start_timer, end_timer):
    st.write("Total running time: ", round(end_timer - start_timer, 3), " seconds")
    with st.expander("Data Protection"):
        st.write(env.APP_WARN_LGPD)


def export_data(df):
    return df.to_csv(index=False).encode("utf-8")


def start():
    page_header()
    start_timer = timer()

    st.subheader("Filter by")

    col_filter1, col_filter2, col_filter3 = st.columns(3)
    with col_filter1:
        uf_df = filter.by_uf()
        uf = st.selectbox("UF", uf_df)

    with col_filter2:
        municipio_df = filter.by_municipio(uf)
        municipio = st.selectbox("Município", municipio_df)

    with col_filter3:
        porte_df = filter.by_porte(uf, municipio)
        porte = st.selectbox("Porte", porte_df)

    st.divider()
    st.subheader("Data Indicators")

    kpi1 = metric.get_value_total_empresas(uf, municipio, porte)
    kpi2 = metric.get_value_total_empresas_individual(uf, municipio, porte)
    kpi3 = metric.get_value_total_empresas_sociedade_anonima(uf, municipio, porte)
    kpi4 = metric.get_value_total_empresas_sociedade_limitada(uf, municipio, porte)
    # kpi5 = metric.get_value_total_empresas_publica(uf, municipio, porte)

    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    col_kpi1.metric("empresas", str(kpi1))
    col_kpi2.metric("empresas individual", str(kpi2))
    col_kpi3.metric("empresas soc anônima", str(kpi3))
    col_kpi4.metric("empresas soc limitada", str(kpi4))

    st.divider()
    st.subheader("Data Aggregate")

    col_agg1, col_agg2 = st.columns(2)
    with col_agg1:
        count_bairro = agg.by_bairro(uf, municipio, porte)
        st.write("Top 5 Bairro", count_bairro)

    with col_agg2:
        count_cnae_fiscal = agg.by_cnae_fiscal(uf, municipio, porte)
        st.write("Top 5 Cnae Fiscal", count_cnae_fiscal)

    st.divider()
    st.subheader("Data Distribution")

    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        with st.container():
            st.write("Companies by matriz filial")
            matriz_filial_df = chart.by_matriz_filial(uf, municipio, porte)
            st.bar_chart(data=matriz_filial_df, x="matriz filial", y="qty")

    with col_chart2:
        with st.container():
            st.write("Companies by opc mei")
            opc_mei_df = chart.by_opc_mei(uf, municipio, porte)
            st.bar_chart(data=opc_mei_df, x="opc mei", y="qty")

    st.divider()
    st.subheader("Data Preview")

    # table_count = table.count_rows(uf, municipio, porte)
    table_head = table.list_rows(uf, municipio, porte)
    table_full = table.export_rows(uf, municipio, porte)

    # st.write("Total Companies found: ", table_count)
    st.write("Listing first 10 Companies", table_head)

    st.download_button(
        label="Export all data",
        data=export_data(table_full),
        file_name=f"empresas_{uf}_{municipio}.csv",
        mime="text/csv",
        key="download-csv",
    )

    st.divider()

    end_timer = timer()
    page_footer(start_timer, end_timer)
