from mongoengine import Document, StringField

class Items(Document):
        url = StringField(required=True)
