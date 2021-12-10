def validate_creation(payload):
  fields = [
  'registry',
  'name'
  ]
  for field in fields:
    if payload[field] is None:
      return { "message": f"Missing {field} parameter in payload"}
  if len(str(payload['registry'])) != 11:
     return { "message": f"Invalid registry number"}

def validate_patch(payload):
  fields = [
  'registry'
  ]
  for field in fields:
    if payload[field] is None:
      return {"message": f"Missing {field} parameter in payload"}

def validate_delete(payload):
  fields = [
  'registry'
  ]
  for field in fields:
    if payload[field] is None:
      return {"message": f"Missing {field} parameter in payload"}