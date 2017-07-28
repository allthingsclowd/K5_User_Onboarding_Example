# Fujitsu Cloud Service K5 IaaS (OpenStack) Demonstration User OnBoarding Portal

## Python Flask Hack

## Author: Graham J Land

Website: https://allthingscloud.eu

Github: @allthingsclowd

This is a very primitive hack by a non developer (me) to produce a working example of how the Fujitsu K5 User Management APIs 
can be leveraged to automate the steps required to add new users to K5 OpenStack.

As a bonus I configured this to run on the Fujitsu K5 Cloud Foundry PaaS Platform

# Installation
- git clone https://github.com/allthingsclowd/K5_User_Onboarding_Example.git
- modify the K5_User_Onboarding_Example/app/templates/hello-flask-login.html to add your K5 Contract details to the dropdown (it currently contains my contracts)
- now, provided you have already installed and configured the cloud foundry agent - https://docs.cloudfoundry.org/cf-cli/install-go-cli.html
- simply issue the following command from the K5_User_Onboarding_Example directory
- cf push
