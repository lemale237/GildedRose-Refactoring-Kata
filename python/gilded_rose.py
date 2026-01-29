# -*- coding: utf-8 -*-

# Item name constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


# Quality bounds
MAX_QUALITY = 50
MIN_QUALITY = 0


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _increase_quality(self, item, amount=1):
        """Increase item quality by amount, respecting max bound."""
        item.quality = min(MAX_QUALITY, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        """Decrease item quality by amount, respecting min bound."""
        item.quality = max(MIN_QUALITY, item.quality - amount)

    def _update_normal_item(self, item):
        """Update a normal item: quality decreases, twice as fast after sell date."""
        item.sell_in -= 1
        degradation = 2 if item.sell_in < 0 else 1
        self._decrease_quality(item, degradation)

    def _update_aged_brie(self, item):
        """Update Aged Brie: quality increases with age, twice as fast after sell date."""
        item.sell_in -= 1
        increase = 2 if item.sell_in < 0 else 1
        self._increase_quality(item, increase)

    def _update_backstage_pass(self, item):
        """Update Backstage pass: quality increases as concert approaches, drops to 0 after."""
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self._increase_quality(item, 3)
        elif item.sell_in < 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)

    def _update_sulfuras(self, item):
        """Update Sulfuras: legendary item, never changes."""
        pass  # Sulfuras never changes

    def update_quality(self):
        """Update quality and sell_in for all items in inventory."""
        for item in self.items:
            if item.name == SULFURAS:
                self._update_sulfuras(item)
            elif item.name == AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == BACKSTAGE_PASSES:
                self._update_backstage_pass(item)
            else:
                self._update_normal_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
