# Stackoverflow-lite-APIs

[StackOverflow-lite](etwtwtrwet) is a platform where users can post questions and provide answers. This is the repo for the backend APIs consumed by the platform.

## Application endpoints

## The following are API enpoints enabling one to:

* Create an accuount
* Login one you create an account
* Post a question
* Get all questions posted
* Get a specific question posted
* Post an answer to a question
* Delete a question
* Mark an answer as the preferred/favorite

## Here is a list of the functioning endpoints

| Endpoint                  | Functionality         | HTTP method |
| ------------------------- | --------------------- | ----------- |
| /api/v1/question          | Post a question       | POST    |
| /api/V1/questions         | Fetch all question    | GET     |
| /api/v1/questions/_q_id_  | Get a question by ID  | GET     |
| /api/v1/answer            | Post an answer        | POST    |
| /api/v1/questions/_q_id_  | Delete a question     | DELETE  |
| /api/v1/q/_q_id_/a/_a_id_ | Mark q as preferred   | PUT     |
| /api/v1/auth/signup       | Register a user       | POST    |
| /api/v1/auth/login        | Log in a user         | POST    |
| /apiv1//auth/logout       | Log out a user        | POST    |

