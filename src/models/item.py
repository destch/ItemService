from .base_object import CreatedObject

from dataclasses import dataclass
from dataclasses import field
from typing import List
from datetime import datetime
from .thumbnail import Thumbnail
from .brand import Brand
import json
#what data does an item have, in the context of how it relates to other parts of the site
#what behavior does an item have, in the context of other objects

#what can an item do?
#items can get added to other things
#a collection can add an item

@dataclass
class Item(CreatedObject):
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
    id: int
    #release_date: datetime
    #price: float
    brand: Brand
    thumbnails: List[Thumbnail]
    #category: str
    #subcategory: str
    #colors: List[str]
    #materials: List[str]

    #consider moving this to the repository file
    def to_json(self):
        """Performs operation blah."""
        dict_rep = {'id': self.id,
                    'name': self.name,
                    'brand': self.brand.name,
                    'thumbnails': [thumbnail.filename for thumbnail in self.thumbnails]}
        return dict_rep
