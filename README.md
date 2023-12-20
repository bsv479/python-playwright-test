# python-playwright-test
Envs configs are located in config/test_config.ini file

## run jenkins 
docker run -p 8090:8080 -p 50000:50000 --restart=on-failure -v /Users/serj/jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk17
## Main LOCAL url:
http://localhost:8080/
## Main PROD url:
https://automationteststore.com

## Run tests parameters:
pytest tests/e2e -v --headed --slowmo 1000 --tracing retain-on-failure --alluredir=allure-results
pytest tests/e2e -v -s --tracing retain-on-failure --alluredir=allure-results

allure serve [directory]