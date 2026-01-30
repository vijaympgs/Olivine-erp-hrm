# Sentry Setup

1. Create project at https://sentry.io
2. Copy DSN
3. Add env var:
   SENTRY_DSN=...
4. Call init_sentry() from wsgi.py / asgi.py
