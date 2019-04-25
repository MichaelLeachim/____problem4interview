# Solution of a task for the interview

## The problem definition

```

Please make a simple page with a payment button and integrate it with coingate.com 
And show all successful and unsuccessful transaction in a list Looking Forward 
for your response and make a very simple document to be easy for anyone to run your project .
( not more than 1, or maximum 2 page )

```

## What is included

* Pagination
* Error handling
* Testing

## What doesn't work

* Ordering by ASC|DESC


## How to install

Copy apps_sample.py in coingate folder into apps.py
And set your api keys there.
For example:

```python

class CoingateConfig(AppConfig):
  name = 'coingate'
  payment_button_link = 'https://coingate.com/pay/name_id_of_test_button'
  api_key_v2 = 'your api key v2'
  api_key_v1 = 'your api key v1'
  api_secret_v1 = 'your api secret v1'
  
```


```shell

virtualenv venv
source venv/bin/activate
pip install -r reqs.txt

```

## How to run (dev mode)

```shell

source venv/bin/activate;
python manage.py runserver;
```


## How to run tests
```shell

source venv/bin/activate;

# if you don't want to hit coingate too much
python manage.py test --exclude-tag=api_call;
# if you want to include hits on coingate
python manage.py test 

```




