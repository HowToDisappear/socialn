# socialn
Simple REST API that allows to:
- singup/ signin users
- create/ modify/ delete posts
- like/ unlike posts
- view listings of users/ posts
- view likes analytics aggregated by day 

### Dependencies
django

djangorestframework

djangorestframework-simplejwt

### Usage
Below are a few examples of HTTPie commands to access “Socialn” API through command line:

To view posts or users:
```
http http://127.0.0.1:8000/api/posts/
http http://127.0.0.1:8000/api/posts/6
http http://127.0.0.1:8000/api/users/3
```
To signup a new user:
```
http --json POST http://127.0.0.1:8000/api/users/signup username="jane" password="jane098123"
```
For authentication we use Simple JWT scheme. To obtain token:
```
http --json POST http://127.0.0.1:8000/api/users/signin/token/obtain username="jane" password="jane098123"
```
Then to make a new post we provide token and post details:
```
http --json POST http://127.0.0.1:8000/api/posts/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTMwNDYxLCJqdGkiOiI0OGE4N2E3YzE1MWE0MGVkODM0NDcxYzJmYjkzMTI4YiIsInVzZXJfaWQiOjd9.BL4iwrDfQ8mseC5JcoCSBXXGs7gz_4Zsqn3C0QeIdM0" title="Hello" body="Hi everyone, nice to meet you all”
```
If our token expires we ask for a refreshed token:
```
http --json POST http://127.0.0.1:8000/api/users/signin/token/refresh refresh=“eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTAxNjU2MSwianRpIjoiYzZiOWM2ZjBmZGRiNGRlYzk3OWUyM2Y4OTM2OGUxYTgiLCJ1c2VyX2lkIjo3fQ.AoTbkUiC7ApuRszPcrZtcPabmr3Jt7DMHhTXRdHYHI8"
```
Afterwards we can like some good post:
```
http --json POST http://127.0.0.1:8000/api/posts/11/like "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTMxMDE3LCJqdGkiOiIxZTBmZTcwMTk0M2M0NGJlYTZlMjZmN2QxNmY1N2FhMCIsInVzZXJfaWQiOjd9.aac5AWyOZXmUkVdfl3xJ8hFiHqW2ZMu8Pm3-j7p0o-8”
```
And finally we can ask for daily count of likes for a specified time period:
```
http http://127.0.0.1:8000/api/posts/analytics/likes/ date_from==2021-04-15 date_to==2021-04-25
```
