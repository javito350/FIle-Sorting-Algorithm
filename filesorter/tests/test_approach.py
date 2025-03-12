"""Confirm that the SortApproach enum works as expected."""

import unittest

from filesorter.approach import SortApproach


class TestSortApproach(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(SortApproach.attrgetter.value, "attrgetter")
        self.assertEqual(SortApproach.bubblesort.value, "bubblesort")
        self.assertEqual(SortApproach.customcompare.value, "customcompare")
        self.assertEqual(SortApproach.lambdafunction.value, "lambdafunction")
        self.assertEqual(SortApproach.quicksort.value, "quicksort")

    def test_enum_names(self):
        self.assertEqual(SortApproach.attrgetter.name, "attrgetter")
        self.assertEqual(SortApproach.bubblesort.name, "bubblesort")
        self.assertEqual(SortApproach.customcompare.name, "customcompare")
        self.assertEqual(SortApproach.lambdafunction.name, "lambdafunction")
        self.assertEqual(SortApproach.quicksort.name, "quicksort")

    def test_enum_membership(self):
        self.assertIn(SortApproach.attrgetter, SortApproach)
        self.assertIn(SortApproach.bubblesort, SortApproach)
        self.assertIn(SortApproach.customcompare, SortApproach)
        self.assertIn(SortApproach.lambdafunction, SortApproach)
        self.assertIn(SortApproach.quicksort, SortApproach)
