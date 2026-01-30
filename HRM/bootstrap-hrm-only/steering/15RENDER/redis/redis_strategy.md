# Redis Caching Strategy

Use Redis for:
- Django cache backend
- Celery broker / result backend
- Feature-flag caching

Recommended keys:
- ff:<feature_key>:<company_id>
- pr:<pr_id>:summary

TTL guidelines:
- Reference data: 24h
- Feature flags: 5 min
- Session caches: 30 min
