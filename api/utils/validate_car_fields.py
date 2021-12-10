def validate_creation(payload):
  fields = [
  'license_plate',
  'type',
  'color',
  'owner_registry'
  ]
  types = [
    'hatch',
    'sedan',
    'convertible'
  ]
  colors = [
    'yellow',
    'blue',
    'gray'
  ]
  for field in fields:
    if payload[field] is None:
      return {"message": f"Missing {field} parameter in payload"}
  if payload['type'] not in types:
    return {"message": "Incorret type parameter in payload"}
  if payload['color'] not in colors:
    return {"message": "Incorret color parameter in payload"}
  if len(payload['license_plate']) > 6:
    return {"message": "Max size of license plate is 6 digits"}

def validate_patch(payload):
  fields = [
  'license_plate'
  ]
  types = [
    'hatch',
    'sedan',
    'convertible'
  ]
  colors = [
    'yellow',
    'blue',
    'gray'
  ]
  for field in fields:
    if payload[field] is None:
      return {"message": f"Missing {field} parameter in payload"}
  if payload['color'] is not None and payload['color'] not in colors:
    return {"message": "Incorret color parameter in payload"}
  if payload['type'] is not None and payload['type'] not in types:
    return {"message": "Incorret type parameter in payload"}


def validate_delete(payload):
  fields = [
  'license_plate'
  ]
  for field in fields:
    if payload[field] is None:
      return {"message": f"Missing {field} parameter in payload"}