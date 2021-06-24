from flask_restful import Resource, reqparse
from models import GpsModel
from app import db
from sqlalchemy import desc


class Gps(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("date", required=True)
        self.parser.add_argument("lat", required=True)
        self.parser.add_argument("long", required=True)

    def get(self):
        res = [q.to_json() for q in GpsModel.query.order_by(GpsModel.date.asc()).all()]
        return res

    def post(self):
        data = self.parser.parse_args()
        print(data["lat"])
        gps = GpsModel(date=data['date'], lat=data['lat'], long=data['long'])
        db.session.add(gps)
        db.session.commit()