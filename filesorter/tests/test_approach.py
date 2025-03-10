"""Confirm that the SortApproach enum works as expected."""

import unittest

from filesorter.approach import SortApproach


class TestSortApproach(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(SortApproach.BY_NAME.value, "by_name")
        self.assertEqual(SortApproach.BY_DATE.value, "by_date")
        self.assertEqual(SortApproach.BY_SIZE.value, "by_size")

    def test_enum_names(self):
        self.assertEqual(SortApproach.BY_NAME.name, "BY_NAME")
        self.assertEqual(SortApproach.BY_DATE.name, "BY_DATE")
        self.assertEqual(SortApproach.BY_SIZE.name, "BY_SIZE")

    def test_enum_membership(self):
        self.assertIn(SortApproach.BY_NAME, SortApproach)
        self.assertIn(SortApproach.BY_DATE, SortApproach)
        self.assertIn(SortApproach.BY_SIZE, SortApproach)
