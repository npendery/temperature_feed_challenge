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

This was a fun challenge! 

A couple notes:
- The frontend application can be found at https://github.com/npendery/loft_temperature_feed_frontend to view the current temperature.
    - There is a lot more I could of done here, but I timeboxed myself and doing the work to wire up a React app with Apollo hopefully showed my knowledge in that space. I swear I can do CSS...even when most of us dont want to :smiling_imp:

- I have a [PR](https://github.com/npendery/loft_temperature_feed_challenge/pull/2/files) open for building out the subscription. I was running into some issues with running the subscription service through `django-channels-graphql-ws`. I always appreciate feedback on how I could do it properly.

- Since I am newer to using Django, it would be great to get some feedback on any conventions I missed.
    - Testing websockets - I didnt test `ExternalApi.ingest_temperatures`, but it would be a good test to add.
    - Test coverage - Where would be some other good tests to add?
    - Docstrings - I want to make sure they are used appropriately and where they should be added.

- Production deployment
    - Ive found AWS Elastic Beanstalk a seamless way to deploy web applications. There are many different options out there though and it really depends on how we care about availability, robustness, scaling, etc.

- Further featureset thoughts
    - Auth layer - A functioning auth layer would be nice to have if this temperature API is private.
    - More robust querying - The rolling average subscription would have been great to add (dang it!) but even some basic querying on average temperature over a time range would be helpful to a consumer
    - Degree scale values - Not everyone uses Fahrenheit! If not a DB column, it would be good to have a query arg that allows conversion to another scale.
    - Notification system - Email or text alerting based on user requirements of temperature going above or below a certain value.

