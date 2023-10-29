from bson import ObjectId


# def serializeDict(a) -> dict:
#     return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) if isinstance(a[i], ObjectId) else a[i] for i in a if i == '_id'},
            **{i: a[i] for i in a if i != '_id'}}
