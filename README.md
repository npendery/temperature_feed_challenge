# Temperature Feed App

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/npendery/loft_temperature_feed_challenge/tree/main.svg?style=svg&circle-token=8b399bac2c48847d8c4ce9f65ae84eaafa7e7cb2)](https://dl.circleci.com/status-badge/redirect/gh/npendery/loft_temperature_feed_challenge/tree/main)


## Setup and run application

#### Copy env from example
```sh
$ cp .env.example .env
```

#### Start services in background 

```sh
$ make run_all
```


#### Start temperature feed

Utilize the GQL mutation request below at the [graph endpoint](localhost:8000/graphql)

#### Create admin user

```sh
$ docker-compose run -ti backend /bin/bash

app# python manage.py createsuperuser --noinput --username adminuser --email admin@example.com
```
#### View Django admin

View the admin portal [here](localhost:8000/admin)

## Available GQL queries

Get current temperature
```graphql
query {
    currentTemperature {
        timestamp
        value
    } 
}
```

Get min and max temperatures for time period
```graphql
query {
    temperatureStatistics(after: "2020-12-06T12:00:00+00:00", before: "2020-12-07T12:00:00+00:00") {
        min
        max
    } 
}
```

Toggle the temperature feed
```graphql
mutation {
    toggleFeed(input: {status: "on"}) {
        status
    } 
}
```


# Challenge Follow Up

This was a fun challenge! There are a couple things I'd like to
