
from .base_object import CreatedObject

from dataclasses import dataclass
from dataclasses import field
from typing import List
from datetime import datetime
#what data does an item have, in the context of how it relates to other parts of the site
#what behavior does an item have, in the context of other objects

#what can an item do?
#items can get added to other things
#a collection can add an item

@dataclass
class Thumbnail(CreatedObject):
    """Item domain object.

    Models the item object within the context of the ClothDB Domain

    Attributes:
        inherits from a created object
        item_id: domain specific identifier
        release_date: the date the object was released to the public
        price: the original price of the object
        brand:
        category:
        subcategory:
        colors:
        materials:
    """
    filename: int
    #release_date: datetime
    #price: float
    #brand: str
    #category: str
    #subcategory: str
    #colors: List[str]
    #materials: List[str]

    def test(self):
        """Performs operation blah."""
        print('aight fam')
