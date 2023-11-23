# python-playwright-test
## run application under test
docker run -d -p 8080:8080 -p 61616:61616 -p 9001:9001 parasoft/parabank
## Main local url
http://localhost:8080/parabank/index.htm
## Main remote url
https://parabank.parasoft.com/parabank/index.htm

## Run tests parameters:
pytest [test_path] -v --headed --slowmo 1000 --tracing retain-on-failure --alluredir=allure-results

allure serve [directory]
