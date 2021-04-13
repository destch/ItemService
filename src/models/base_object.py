#TODO implement/think of a way to incorporate possibility of edits/editable objects
#maybe add an image attribute/images attribute that maps to an Image objecti
#can implement common functions as abstract base class objects
class CreatedObject:
    """A domain object to represent an object which has been added to ClothDB

    For example, a collection, a brand, an item. Used to facilitiate business
    logic surrounding contributed objects.

    For now I am thinking user, item, collection, brand, fit, style, material, etc..

    Attributes:
        name: the name of the object
        description: describes the object
        created_at: datetime when the object was introduced to ClothDB
    """
    def __init__(self, name, description, created_at):
        self.name = name
        self.description = description
        self.created_at = created_at


