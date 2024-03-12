import marshmallow as ma


class ParticipantSchema(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()


class CategorySchema(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()


class ResultsSchema(ma.Schema):
    id = ma.fields.Integer()
    participant1 = ma.fields.Nested(ParticipantSchema)
    participant2 = ma.fields.Nested(ParticipantSchema)
    category = ma.fields.Nested(CategorySchema)
    result = ma.fields.Float()
