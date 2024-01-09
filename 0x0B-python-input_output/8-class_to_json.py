#!/usr/bin/python3
"""Defines of python class-to-JSON function."""


def class_to_json(obj):
    """returns dictionary represntation of simple data struct"""
    return obj.__dict__
