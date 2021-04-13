import abc
from models import Item


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(batch)

    def get(self, item_id):
        return self.session.query(Item).filter_by(reference=item_id).one()

    def list(self):
        return self.session.query(model.Batch).all()
