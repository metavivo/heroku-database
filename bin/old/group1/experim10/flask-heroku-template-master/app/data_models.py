from app.extensions import db

class ExampleOrmClass(db.Model):
    __tablename__ = 'example'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return '<ExampleOrmClass %r>' % (self.name)
