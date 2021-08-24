# -*- coding: utf-8 -*-
# Copyright (c) 2021 Interstellio (PTY) LTD - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
from pytest import raises
import pytest
parametrize = pytest.mark.parametrize

from mysqlchk import metadata

class TestMetadata(object):
    def test_package_name(self):
        assert metadata.package == 'luxon'

    def test_identity(self):
        assert 'Luxon' in metadata.identity

    def test_classifiers(self):
        assert isinstance(metadata.classifiers, list)
