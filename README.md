# All the forests :deciduous_tree: :deciduous_tree: :deciduous_tree:


You can view the project on https://marhaban.samatar.dev

This service is running on cloud run (first time!) and it's connected to a cloud sql instance.
## You can install the project's dependencies by running:

```
(pip install pipenv) -- if you don't have pipenv

pipenv install --dev
```

I actually don't run the api locally as I'm used to developing against production apis.
If you do want to run the api locally, you can build the docker image:
```
docker build -t forests .

docker run -p 8000:8000 forests
```

Before this step you also need to have a postgres database running locally, I use a docker file for this:

```
FROM postgres:12

ENV POSTGRES_DB=forests
ENV POSTGRES_USER=forests
ENV POSTGRES_HOST_AUTH_METHOD=trust
```

To run database migrations:

```
pipenv run alembic upgrade head
```

To run tests:

```
pipenv run pytest
```
