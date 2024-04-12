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