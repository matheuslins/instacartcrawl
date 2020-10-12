# Instacart Crawl

A spider from [Instacart!](https://www.instacart.com/)

The spider capture the products of the first store in the account.

To broken the Recaptcha has used the [2Captcha ](https://2captcha.com/) system, 
so it's necessary to set the API KEY as environment vars.
 
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
2CAPTCHA_URL=https://2captcha.com/in.php
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

## Tools used

    - Python 3.7
    - 2Captcha (To broken recaptcha)
    - AIOHTTP (To create a server and making async requests)

## The Process

While the process I've used the Pomodoro methodology. I took breaks of 5 minutes and hands-on of 30min. Was important it because some times
I wasn't redeeming anymore as in the beginning. So, theses break moments make me more relaxing to start again.

In the beginning, I had a limitation because the Instacart Store isn't in my region. So, I had to find a postcode from the USA. I got a postcode code from New York and made the signup with it and my personal email.

The postcode used: 10040

#### Best Practices

I always tried to use clean code and architecture best practices.
So, you will see here an organization based on limits, resources, business, and also:

- Clean Names
- Code Delimitations
- Unique Responsibilities


## The Challenges

My first difficult was to get the access_token. I needed it to build a login request. After some minutes of searching, I found it and merging
with the captcha token has taken through the 2Captcha system, was possible to gain a instacart session.

After that, I took some hours to discovery how to get the data. It was a litter difficult because the site has an API navegation
and use javascript to load the data on the page. So, I needed to understand the API flow, but I got it!

