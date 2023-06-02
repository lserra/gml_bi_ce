#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import yaml
from yaml.loader import SafeLoader

import dash_tool
from config import Config
from src.auth.authenticate import Authenticate

# Initializing objects
env = Config()

if __name__ == "__main__":
    # Loading config file
    with open(f"{env.APP_PATH}/config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Creating the authenticator object
    authenticator = Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    # creating a login widget
    name, authentication_status, username = authenticator.login("Login", "sidebar")
    if authentication_status:
        authenticator.logout("Logout", "sidebar")
        st.write(f"Welcome, **_{str(name).upper()}_**")
        dash_tool.start()
    elif authentication_status is False:
        st.error("Username/password is incorrect")
    elif authentication_status is None:
        st.warning("Please enter your username and password")
