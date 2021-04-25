from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import mapper, relationship, registry, sessionmaker
from src.models import item, brand, base_object, thumbnail
from datetime import datetime
import os

def setup_orm():
    mapper = registry()
    metadata = MetaData()

    items = Table(
        "items",
        metadata,
        Column("id", primary_key=True),
        Column("name"),
        Column("deleted", Intege),
        Column("description"),
        Column("brand_id", Integer, ForeignKey("brands.id"))
    )

    brands = Table(
        "brands",
        metadata,
        Column("id", primary_key=True),
        Column("name")
    )

    thumbnails = Table(
        "thumbnails",
        metadata,
        Column("id", primary_key=True),
        Column("filename"),
        Column("item_id", Integer, ForeignKey("items.id"))
    )

    def start_mappers():
        mapper.map_imperatively(
            item.Item,
            items,
            properties={
                "thumbnails": relationship(
                    thumbnail.Thumbnail, backref="item", order_by=thumbnails.c.id
                )
            }
        )
        mapper.map_imperatively(
            brand.Brand,
            brands,
            properties={
                "items": relationship(
                    item.Item, backref="brand", order_by=items.c.id
                )
            },
        )
        mapper.map_imperatively(thumbnail.Thumbnail, thumbnails)

    start_mappers()


def db():
    user = os.environ.get('DB_USER')
    pw = os.environ.get('DB_PW')
    engine = create_engine('postgresql://{}:{}@ec2-34-198-0-244.compute-1.amazonaws.com/ClothDB_DEV'.format(user, pw))
    DBSession = sessionmaker(bind=engine)
    return DBSession
