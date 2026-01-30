# Procurement Celery Tasks
from celery import shared_task

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3})
def notify_pr_created(self, pr_id):
    """Async notification when PR is created"""
    # placeholder: email / webhook / audit log
    return f"PR {pr_id} notification dispatched"



