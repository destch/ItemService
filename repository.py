import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError


    results = session().query(item.Item).order_by(item.Item.id.desc()).limit(16).all()
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(item)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self, order_by=None, limit=None, pagination=None, page=1):
        base_query = self.session.query(item.Item)
        if order_by:
            self.session.query
       if paginate:

        return self.session.query(item.Item).all()
