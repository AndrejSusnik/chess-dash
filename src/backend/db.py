from pony.orm import Database, Required, Set, PrimaryKey, Optional

db = Database("sqlite", "db.sqlite", create_db=True)


class Participant(db.Entity):  # type: ignore
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    categories = Set('Category')  # type: ignore
    results = Set('Result')    # type: ignore


class Category(db.Entity):  # type: ignore
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Optional(str)
    participants = Set(Participant)


class Result(db.Entity):  # type: ignore
    id = PrimaryKey(int, auto=True)
    result = Required(float)
    participants = Set(Participant)


db.generate_mapping(create_tables=True)
