import json
    
def to_json(obj: object, pretty_print=False) -> str:
    if not pretty_print:
        return json.dumps(obj, default=lambda o: o.__json__())
    else:
        return json.dumps(obj, default=lambda o: o.__json__(), indent=4)