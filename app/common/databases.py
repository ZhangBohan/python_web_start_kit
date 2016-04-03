from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class CommonColumnMixin(object):
    id = db.Column(db.BigInteger, primary_key=True)
    created_on = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    updated_on = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))


class Base(CommonColumnMixin, db.Model):
    __abstract__ = True

    def __repr__(self):
        return '<%s(id=%s)>' % (self.__class__.__name__, self.id)
