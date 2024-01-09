import pytest
from os.path import isfile
from os import access, R_OK

file = '../test.csv'


def test_file():
    assert isfile(file) and access(file, R_OK), \
        f'File doesnt exist or is not readable'


def test_expected_data():
    expected_final_data = ['Company', 'Date', 'Price', 'Currency', 'Location'
                           'Lenzing', '170447112', '34.75', 'EUR', 'Vienna'
                           'Andritz', '170447131', '59.41', 'USD', 'New York'
                           'EVN', '170447132', '28.55', 'EUR', 'Vienna'
                           'EVN', '170447133', '31.18', 'USD', 'New York']
    assert read_data == expected_data


def test_data_format():
    for row in read_data:
        assert len(row) == 5
