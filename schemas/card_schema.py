from main import ma 

#create the Card Schema with Marshmallow, it'll provide the serialisation needed for converting data into JSON
class CardSchema(ma.Schema):
    class Meta:
        #Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority")

#single card schema, when one card needs to be retrieved
card_schema = CardSchema()
#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)


