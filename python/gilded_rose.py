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

    def update_quality(self):
        for item in self.items:
            if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
                if item.quality > 0:
                    if item.name != SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == BACKSTAGE_PASSES:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE_PASSES:
                        if item.quality > 0:
                            if item.name != SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
