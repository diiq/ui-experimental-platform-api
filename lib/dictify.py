import datetime


def dictify(o):
    if hasattr(o, "public_dict"):
        return dictify(o.public_dict())

    if hasattr(o, "__call__"):
        return dictify(o())

    if isinstance(o, dict):
        return {k: dictify(v) for k, v in o.iteritems()}

    if hasattr(o, "__iter__"):
        return [dictify(v) for v in o]

    if isinstance(o, datetime.datetime):
        return o.isoformat()

    else:
        return o
