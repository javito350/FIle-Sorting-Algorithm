"""Test the sorting functions in the organize module."""

import pytest

from filesorter.organize import (
    sort_persons,
    sort_persons_attrgetter,
    sort_persons_bubblesort,
    sort_persons_customcompare,
    sort_persons_lambdafunction,
    sort_persons_quicksort,
)
from filesorter.person import Person


@pytest.fixture
def persons_list():
    """Create a list of Person objects for testing as a fixture."""
    return [
        Person("Alice", "USA", "1234567890", "Engineer", "alice@example.com"),
        Person("Bob", "UK", "0987654321", "Doctor", "bob@example.com"),
        Person(
            "Charlie", "Canada", "5555555555", "Artist", "charlie@example.com"
        ),
    ]


def test_sort_persons_attrgetter(persons_list):
    sorted_list = sort_persons_attrgetter(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_bubblesort(persons_list):
    sorted_list = sort_persons_bubblesort(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_customcompare(persons_list):
    sorted_list = sort_persons_customcompare(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_lambdafunction(persons_list):
    sorted_list = sort_persons_lambdafunction(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_quicksort(persons_list):
    sorted_list = sort_persons_quicksort(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_dispatch_bubblesort(persons_list):
    sorted_list = sort_persons(persons_list, "name", "bubblesort")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_dispatch_quicksort(persons_list):
    sorted_list = sort_persons(persons_list, "name", "quicksort")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_dispatch_lambdafunction(persons_list):
    sorted_list = sort_persons(persons_list, "name", "lambdafunction")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_dispatch_attrgetter(persons_list):
    sorted_list = sort_persons(persons_list, "name", "attrgetter")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_dispatch_customcompare(persons_list):
    sorted_list = sort_persons(persons_list, "name", "customcompare")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_invalid_approach(persons_list):
    with pytest.raises(ValueError, match="Unknown sorting approach: invalid"):
        sort_persons(persons_list, "name", "invalid")
