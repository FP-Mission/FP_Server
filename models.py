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

class PictureModel(db.Model):
    __tablename__ = 'picture'

    id = db.Column(db.Integer, primary_key=True)
    picturI_id = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.Integer, unique=True, nullable=False)

    def to_json(self):
        return {"id":self.picturI_id, "date" : self.date}