import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import os

def init_sentry():
    dsn = os.getenv("SENTRY_DSN")
    if not dsn:
        return

    sentry_sdk.init(
        dsn=dsn,
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.1,
        send_default_pii=True,
        environment=os.getenv("ENVIRONMENT", "production"),
    )



