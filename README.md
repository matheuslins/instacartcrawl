# Instacart Crawl

A spider from [Instacart!](https://www.instacart.com/)

The spider capture the products of the first store in the account.

To broken the Recaptcha has used the [2Captcha ](https://2captcha.com/) system, 
so it's necessary to set the API KEY as environment vars.

![Kibana Products Dashboard](img/es.png)
 
### Environment vars

First of all, create `.env` file in the root of the project and set all environment vars. 
See the `.env-example` file

1 - Auth credentials of Instacart Site

````.env
AUTH_USER=
AUTH_PASSWORD=
````

2 - The 2Captcha API KEY

````.env
2CAPTCHA_API_KEY=
2CAPTCHA_URL=https://2captcha.com/in.php
````

3 - Save products on DB (ElasticSearch)

````.env
SAVE_DB_ITEM=True
````

### Pre Run

Create a virtualenv and install dependencies: ```make setup``` 

### Running

To run, use:

````python
make run
````

To run using docker, you can use:

````python
make run-docker
````

Your server is running: http://0.0.0.0:8080

### Instacart Spider

Just access: http://0.0.0.0:8080/instacart

#### Kibana

If you set `SAVE_DB_ITEM=True` and executed `make run-docker` you can see all products on Kibana here: http://localhost:5601/app/discover#/

## TODO

```
1 - Create a Dashboard where is possible to see the processing of scraping in real-time
2 - Unit Tests
3 - Treat all exceptions
```

