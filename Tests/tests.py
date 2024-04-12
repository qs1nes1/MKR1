import pytest

from tasks import read_population_data, calculate_population_change

@pytest.fixture
def sample_population_data():
    data = """
    Ukraine, 2000, 48000000
    Ukraine, 2010, 46000000
    USA, 2000, 281000000
    USA, 2010, 309000000
    """
    return data.strip()

def test_read_population_data(sample_population_data):
    expected_data = {
        'Ukraine': [(2000, 48000000), (2010, 46000000)],
        'USA': [(2000, 281000000), (2010, 309000000)]
    }
    result = read_population_data(sample_population_data)
    assert result == expected_data