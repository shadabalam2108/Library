from marshmallow import Schema, fields

class Members_schema(Schema):
    id = fields.Int()
    name=fields.Str()
    password = fields.Str()
    email = fields.Email()
    membership_status = fields.Str(allow_none=True, validate=lambda s: s in [None, "admin"])


class Books_schema(Schema):
    id = fields.Int()
    title = fields.Str()
    publication_date = fields.Str()
    genre = fields.Str()
    count=fields.Int()
    author_name = fields.Str ()
   

class Authors_schema(Schema):
    name = fields.Str()
    bio = fields.Str()
    dob = fields.Str()