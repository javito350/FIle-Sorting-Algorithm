"""Test suite for the constants module."""

# ruff: noqa: PLR2004

from filesorter import constants


def test_constant_values_for_person_attributes():
    """Ensure that all of the person_attributes constants have a value."""
    assert len(vars(constants.person_attributes).items()) == 5
    for _, value in vars(constants.person_attributes).items():
        assert value is not None


def test_constant_values_for_person_index():
    """Ensure that all of the person_index constants have a value."""
    assert len(vars(constants.person_index).items()) == 5
    for _, value in vars(constants.person_index).items():
        assert value is not None


def test_person_attributes_values():
    """Ensure that person_attributes constants have correct values."""
    assert constants.person_attributes.Name == "name"
    assert constants.person_attributes.Country == "country"
    assert constants.person_attributes.Phone_Number == "phone_number"
    assert constants.person_attributes.Job == "job"
    assert constants.person_attributes.Email == "email"


def test_person_index_values():
    """Ensure that person_index constants have correct values."""
    assert constants.person_index.Name == 0
    assert constants.person_index.Country == 1
    assert constants.person_index.Phone_Number == 2
    assert constants.person_index.Job == 3
    assert constants.person_index.Email == 4
