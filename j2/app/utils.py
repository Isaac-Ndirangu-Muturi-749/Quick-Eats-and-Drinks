# app/utils.py
from flask import Flask

def format_currency(value):
    """Formats a number as currency"""
    return "${:,.2f}".format(value)

def register_filters(app):
    app.jinja_env.filters['format_currency'] = format_currency
