from app import db

class GpsModel(db.Model):
    __tablename__ = 'gps'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, unique=True, nullable=False)
    lat = db.Column(db.Float,nullable=False)
    long = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(30), nullable=False)

    def to_json(self):
        return {"date":self.date, "lat" : self.lat, "long": self.long, "name":self.name}