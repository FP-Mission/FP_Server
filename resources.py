from flask_restful import Resource, reqparse
from models import GpsModel, PictureModel
from app import db
import base64
from datetime import datetime


class Gps(Resource):
    def __init__(self):
        self.parser_post = reqparse.RequestParser()
        self.parser_post.add_argument("date", required=True)
        self.parser_post.add_argument("lat", required=True)
        self.parser_post.add_argument("long", required=True)
        self.parser_post.add_argument("name", required=True)

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
        try:
            gps = GpsModel(date=data['date'], lat=data['lat'], long=data['long'],name=data['name'])
            db.session.add(gps)
            db.session.commit()
        except:
            print("gps already saved")

class Picture(Resource):
    def __init__(self):
        self.parser_post = reqparse.RequestParser()
        self.parser_post.add_argument("id", required=True)
        self.parser_post.add_argument("picture", required=True)

        self.parser_get = reqparse.RequestParser()
        self.parser_get.add_argument("dump", type=int)

    def get(self):
        data = self.parser_get.parse_args()
        if data['dump'] == None:
            res = [q.to_json() for q in PictureModel.query.order_by(PictureModel.date.asc()).all()]
            return res
        elif data['dump'] == 1:
            PictureModel.query.delete()
            db.session.commit()
            return "Picture table dump"

    def post(self):
        data = self.parser_post.parse_args()
        epoch = datetime.timestamp(datetime.now())
        img = base64.b64decode(data['picture'].encode('utf-8'))
        with open(f"static/img/{data['id']}.jpg", "wb") as f:
            f.write(img)
        try:
            picture = PictureModel(picturI_id=data['id'],date=int(epoch))
            db.session.add(picture)
            db.session.commit()
        except:
            print("picture already saved")
