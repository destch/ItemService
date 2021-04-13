from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import mapper, relationship, registry, sessionmaker
from models import item, brand, base_object
from datetime import datetime

mapper = registry()
metadata = MetaData()

items = Table(
    "items",
    metadata,
    Column("id", primary_key=True),
    Column("name"),
    Column("description"),
    Column("brand_id", Integer, ForeignKey("brands.id"))
)

brands = Table(
    "brands",
    metadata,
    Column("id", primary_key=True),
    Column("name")
)

def start_mappers():
    mapper.map_imperatively(item.Item, items)
    mapper.map_imperatively(
        brand.Brand,
        brands,
        properties={
            "items": relationship(
                item.Item, backref="brand", order_by=items.c.id
            )
        },
    )

start_mappers()


engine = create_engine('postgresql://danielchavez:daniel97@ec2-34-198-0-244.compute-1.amazonaws.com/ClothDB_DEV')


DBSession = sessionmaker(bind=engine)
session = DBSession()
results = session.query(item.Item).limit(10).all()
print(results[0].brand)

