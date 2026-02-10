import os
import unittest

import certifi


class TestCertifi(unittest.TestCase):
    def test_cabundle_exists(self) -> None:
        assert os.path.exists(certifi.where())

    def test_read_contents(self) -> None:
        content = certifi.contents()
        assert "-----BEGIN CERTIFICATE-----" in content

    def test_py_typed_exists(self) -> None:
        assert os.path.exists(
            os.path.join(os.path.dirname(certifi.__file__), 'py.typed')
        )

    def test_globaltrust_2020_removed(self) -> None:
        """Test that GLOBALTRUST 2020 certificate has been removed (CVE-2024-39689)"""
        content = certifi.contents()
        assert "GLOBALTRUST 2020" not in content
        assert "e-commerce monitoring GmbH" not in content
