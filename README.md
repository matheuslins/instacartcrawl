# Instacart Crawl

A spider from [Instacart!](https://www.instacart.com/)

The spider capture the products of the first store in account.

To broken the recaptcha was used [2Captcha ](https://2captcha.com/) system, so
it's necessary set the api key as environment vars.
 
### Environment vars

First of all, set all environment vars. See the `.env-example` file

1 - Auth credentials of Instacart Site

````.env
AUTH_USER=
AUTH_PASSWORD=
````

2 - The 2Captcha API KEY

````.env
2CAPTCHA_API_KEY=
````

### Pre Run

Create a virtualenv and install dependencies: ```make setup``` 

### Running

To run using docker, tou can use:

````python
make run-docker
````

To a normal running:

````python
make run
````

Your server is running: http://0.0.0.0:8080

### Instacart Spider

Just access: http://0.0.0.0:8080/instacart