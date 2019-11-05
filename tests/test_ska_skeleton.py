#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the ska_python_skeleton module."""
import pytest

from ska_python_skeleton import main


# TODO: Replace all the following examples with tests for the ska_python_skeleton package code
def test_something():
    """Example: Assert with no defined return value."""
    assert True


def test_with_error():
    """Example: Assert raising error."""
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise ValueError


# Fixture example
@pytest.fixture
def an_object():
    """Example: Define fixture for subsequent test."""
    return {}


def test_ska_python_skeleton(an_object):
    """Example: Assert fixture return value."""
    assert an_object == {}


def test_package():
    """Example: Assert the ska_python_skeleton package code."""
    assert main.example() is None
    assert main.testing_example() == 2
