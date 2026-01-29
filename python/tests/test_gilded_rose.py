# -*- coding: utf-8 -*-
"""
Unit tests for Gilded Rose kata.
These tests document the expected behavior based on the requirements specification.
"""
import pytest
from gilded_rose import Item, GildedRose


class TestNormalItem:
    """Tests for regular items that degrade in quality over time."""

    def test_quality_decreases_by_1_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 19

    def test_sell_in_decreases_by_1(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].sell_in == 9

    def test_quality_decreases_twice_as_fast_after_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 18

    def test_quality_never_goes_negative(self):
        items = [Item("Normal Item", 5, 0)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    def test_quality_never_goes_negative_after_sell_date(self):
        items = [Item("Normal Item", -1, 1)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0


class TestAgedBrie:
    """Tests for Aged Brie which increases in quality over time."""

    def test_quality_increases_with_age(self):
        items = [Item("Aged Brie", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 21

    def test_quality_increases_twice_after_sell_date(self):
        items = [Item("Aged Brie", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 22

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 10, 50)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50

    def test_quality_never_exceeds_50_even_after_sell_date(self):
        items = [Item("Aged Brie", -1, 49)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50

    def test_sell_in_decreases(self):
        items = [Item("Aged Brie", 5, 10)]
        GildedRose(items).update_quality()
        assert items[0].sell_in == 4


class TestSulfuras:
    """Tests for Sulfuras, a legendary item that never changes."""

    def test_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        assert items[0].quality == 80

    def test_sell_in_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        assert items[0].sell_in == 10

    def test_quality_stays_80_even_with_negative_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        GildedRose(items).update_quality()
        assert items[0].quality == 80


class TestBackstagePasses:
    """Tests for Backstage passes which increase in quality as concert approaches."""

    def test_quality_increases_by_1_when_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 21

    def test_quality_increases_by_2_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 22

    def test_quality_increases_by_2_when_6_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 22

    def test_quality_increases_by_3_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 23

    def test_quality_increases_by_3_when_1_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 23

    def test_quality_drops_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    def test_quality_stays_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    def test_quality_never_exceeds_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50

    def test_sell_in_decreases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].sell_in == 9


class TestConjuredItem:
    """
    Tests for Conjured items which degrade in quality twice as fast as normal items.
    """

    def test_quality_degrades_twice_as_fast_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 18  # -2 instead of -1

    def test_quality_degrades_four_times_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 16  # -4 instead of -2

    def test_quality_never_goes_negative(self):
        items = [Item("Conjured Mana Cake", 5, 1)]
        GildedRose(items).update_quality()
        assert items[0].quality >= 0

    def test_sell_in_decreases(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        GildedRose(items).update_quality()
        assert items[0].sell_in == 4


class TestMultipleItems:
    """Tests to verify multiple items are updated correctly."""

    def test_updates_all_items(self):
        items = [
            Item("Normal Item", 5, 10),
            Item("Aged Brie", 5, 10),
            Item("Sulfuras, Hand of Ragnaros", 5, 80),
        ]
        GildedRose(items).update_quality()

        assert items[0].quality == 9   # Normal: -1
        assert items[1].quality == 11  # Aged Brie: +1
        assert items[2].quality == 80  # Sulfuras: unchanged


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
