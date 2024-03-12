import marshmallow as ma


class ParticipantSchema(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()


class ParticipantQuerySchema(ma.Schema):
    id = ma.fields.Integer()


class ParticipantPostSchema(ma.Schema):
    name = ma.fields.String()


class CategorySchema(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()
    description = ma.fields.String(default=None)


class CategoryQuerySchema(ma.Schema):
    id = ma.fields.Integer()


class CategoryPostSchema(ma.Schema):
    name = ma.fields.String()
    description = ma.fields.String(default=None)


class ResultSchema(ma.Schema):
    id = ma.fields.Integer()
    participant1 = ma.fields.Nested(ParticipantSchema)
    participant2 = ma.fields.Nested(ParticipantSchema)
    category = ma.fields.Nested(CategorySchema)
    result = ma.fields.Float()


class ResultPostSchema(ma.Schema):
    participant1 = ma.fields.Nested(ParticipantQuerySchema)
    participant2 = ma.fields.Nested(ParticipantQuerySchema)
    category = ma.fields.Nested(CategoryQuerySchema)
    result = ma.fields.Float()


class ResultQuerySchema(ma.Schema):
    id = ma.fields.Integer()
