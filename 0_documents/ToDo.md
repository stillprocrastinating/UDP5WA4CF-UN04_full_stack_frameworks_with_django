# To Do

- In _settings.py_, use `SECRET_KEY = os.environ.get("SECRET_KEY")`
- In _settings.py_, use `DEBUG = os.environ.get("DEBUG", False)`
- 404.html < 4_templates
- Use `0_` and `1_` naming conventions for ease of use
- In _settings.py_, use `ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", ['.127.0.0.1', '.herokuapp.com', 'https://fireship.dev/amiresponsive',])` <!-- unsure of AmIResponsive functionality, just try it -->


## Design

- Subscription to lessons; tiers = classes.
- Validation on payments to prevent multiple subscriptions to the same class with the same student. GDPR: student_1, student_2... <!-- initials? -->
- One-off payments for lessons & show tickets, validated by date. Multiple payments possible after a warning confirmation.


## Installs

`pip freeze > requirements.txt`
`pip install -r requirements.txt`