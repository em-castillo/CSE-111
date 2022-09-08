'''W05 Team Assignment - Testing'''


from names import make_full_name, extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Tim", "Strobell") == "Strobell; Tim"
    assert make_full_name("Bob", "Johnson") == "Johnson; Bob"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Strobell; Tim") == "Strobell"
    assert extract_family_name("Johnson; Bob") == "Johnson"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Strobell; Tim") == "Tim"
    assert extract_given_name("Johnson; Bob") == "Bob"
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
