# Step 1 — Clean Celery Wiring (Procurement)

Principles:
- No Celery in views/serializers
- Use service + domain events
- Fire tasks only after DB commit

Flow:
Service -> Domain Event -> transaction.on_commit -> Celery task

This ensures stability and rollback safety.
