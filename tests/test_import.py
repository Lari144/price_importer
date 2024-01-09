from os.path import isfile
from os import access, R_OK
from src import Import
import pandas

file = '../test.csv'
importer = Import(file)


def test_file():
    assert isfile(file) and access(file, R_OK), \
        f'File doesnt exist or is not readable'


def test_expected_data():
    expected_final_data = pandas.DataFrame({
        'Company': ['Lenzing', 'Andritz', 'EVN', 'EVN'],
        'Date': [170447112, 170447131, 170447132, 170447133],
        'Price': [34.75, 59.41, 28.55, 31.18],
        'Currency': ['EUR', 'USD', 'EUR', 'USD'],
        'Location': ['Vienna', 'New York', 'Vienna', 'New York']
    })
    pandas.testing.assert_frame_equal(
        importer.read_data(), expected_final_data)


def test_data_format():
    for _, row in importer.read_data().iterrows():
        assert len(row) == 5
