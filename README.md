# Carford Town

### Description
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

### Technologies
Project is created with:
* Python
* Flask
* SQLAlchemy
* Docker

## Setup
To run this project, fill the .env with the requested variables,then run:

```
docker build . -t carford 
docker-compose up -d 
```