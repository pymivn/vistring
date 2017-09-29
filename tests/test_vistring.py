#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `vistring` package."""

import pytest


from vistring import vistring


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    assert vistring.remove_tones('trăm năm trong cõi người ta') \
        == 'tram nam trong coi nguoi ta'
    assert vistring.remove_tones('chữ tài chữ mệnh khéo là ghét nhau') \
        == 'chu tai chu menh kheo la ghet nhau'
