import json
    
def to_json(obj: object) -> str:
    return json.dumps(obj, default=lambda o: o.__json__(), indent=4)