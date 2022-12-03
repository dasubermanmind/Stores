## Quick Start to run the API

1. Create virtualenv
1. `pip install -r requiremnts.txt`
1. flask run


## Docker setup (optional)
1. Run `docker build -t rest-store-api` . 
1. Once the container has been built we then run it via `docker run -dp 5000:5000 rest-store-api`



Now you can test each individual endpoints independantly.

## Todo's

1. Version the API []
1. Add Users Functionality []
1. Add middleware JWT []
1. Add SQLAlchemy []
1. Integrate with Postgres []
1. Integrate with Docker [X]
1. Integrate with Celery []
1. Maybe add the SIMPLETL as part of the process?? [] 