'''W05 Team Activity - Testing - Stretch Challenges'''

from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    assert extract_city("1234 Alpha, Beta, CA 12345") == "Beta"


def test_extract_state():
    assert extract_state("1234 Alpha, Beta, CA 12345") == "CA"


def test_extract_zipcode():
    assert extract_zipcode("1234 Alpha, Beta, CA 12345") == "12345"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
