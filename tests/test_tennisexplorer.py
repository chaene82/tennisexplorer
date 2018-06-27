#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tennisexplorer` package."""

import pytest

from click.testing import CliRunner

from tennisexplorer import tennisexplorer
from tennisexplorer import cli
from tennisexplorer import get_te_player


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'tennisexplorer.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_player():
    """Test player part"""
    df_player = get_te_player()
    assert len(df_player) == 1
    
    
def test_player():
    """Test player part"""
    matchlist = get_te_matchlist(year = '2018', month = '05', day = '07', match_type="atp-single")
    assert len(matchlist) == 174   