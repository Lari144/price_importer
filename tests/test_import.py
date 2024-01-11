from os.path import isfile
from os import access, R_OK
from src import Import, Visualize
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


def test_data_types():
    data = importer.read_data()
    assert pandas.api.types.is_numeric_dtype(
        data['Price']), "Price column is not numeric"
    assert pandas.api.types.is_numeric_dtype(
        data['Date']), "Date column is not datetime type"


def test_grouping_logic():
    data = importer.read_data()
    grouped = data.groupby(['Company', 'Location'])['Price'].mean()
    assert 'Company' in grouped.index.names, "Grouping by Company failed"
    assert 'Location' in grouped.index.names, "Grouping by Location failed"
