from flask_restful import Resource, reqparse
from models import GpsModel
from app import db


class Gps(Resource):
    def __init__(self):
        self.parser_post = reqparse.RequestParser()
        self.parser_post.add_argument("date", required=True)
        self.parser_post.add_argument("lat", required=True)
        self.parser_post.add_argument("long", required=True)

        self.parser_get = reqparse.RequestParser()
        self.parser_get.add_argument("dump", type=int)


    def get(self):
        data = self.parser_get.parse_args()
        if data['dump'] == None:
            res = [q.to_json() for q in GpsModel.query.order_by(GpsModel.date.asc()).all()]
            return res
        elif data['dump'] == 1:
            GpsModel.query.delete()
            db.session.commit()
            return "Gps table dump"

    def post(self):
        data = self.parser_post.parse_args()
        print(data["lat"])
        gps = GpsModel(date=data['date'], lat=data['lat'], long=data['long'])
        db.session.add(gps)
        db.session.commit()