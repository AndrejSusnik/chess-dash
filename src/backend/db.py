from pony import orm

db = orm.Database("sqlite", "db.sqlite", create_db=True)


class Participant(db.Entity):  # type: ignore
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    results = orm.Set("Results", reverse='participant1')  # type: ignore


class Category(db.Entity):  # type: ignore
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)


class Results(db.Entity):  # type: ignore
    id = orm.PrimaryKey(int, auto=True)
    participant1 = orm.Required(Participant)
    participant2 = orm.Required(Participant)
    category = orm.Required(Category)
    result = orm.Required(float)


db.generate_mapping(create_tables=True)
