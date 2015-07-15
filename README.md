# WebUI automated tests for ownCloud

Suite of tests and needed utilities to be runned for testing the web interface of ownCloud.

It uses python as main language and selenium webdriver.

We are focused on Firefox webdriver for now.


Status:
- Scrutinizer: [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/owncloud/webui-tests/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/owncloud/webui-tests/)

- Travis: [![Scrutinizer Code Quality](https://travis-ci.org/owncloud/webui-tests.svg?branch=master)](https://travis-ci.org/owncloud/webui-tests)


#Prepare environment

Previous requirements: virtualenv

If virtualenv is not installed do

```
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz
$ tar xvfz virtualenv-X.X.tar.gz
$ cd virtualenv-X.X
$ [sudo] python setup.py install
```


Now we can start:
```
virtualenv selenium
source selenium/bin/activate
pip install -r requirements.txt
```


Create config file using **config.py_sample** as example and name it **config.py**.

#Run tests

with virtualenv activated do python runtests.py



#Authors

Sergio Bertolín (@SergioBertolinSG)

David Toledo (@davitol)
