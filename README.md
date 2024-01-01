# Temperature Feed App

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/npendery/loft_temperature_feed_challenge/tree/main.svg?style=svg&circle-token=8b399bac2c48847d8c4ce9f65ae84eaafa7e7cb2)](https://dl.circleci.com/status-badge/redirect/gh/npendery/loft_temperature_feed_challenge/tree/main)

## Setup and run

### Copy env from example
```sh
$ cp .env.example .env
```

### Start services in background 

```sh
$ docker-compose up -d
```

### Create admin user

```sh
$ docker exec -ti temperature_backend /bin/bash

app# python manage.py createsuperuser --noinput --username adminuser --email admin@example.com
```


## Queries to run


```graphql
query {
    currentTemperature {
        timestamp
        value
    } 
}

query {
    temperatureStatistics(after: "2020-12-06T12:00:00+00:00", before: "2020-12-07T12:00:00+00:00") {
        min
        max
    } 
}
```

