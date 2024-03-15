from celery import Celery
from celery.schedules import crontab

app = Celery('music_recognition_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'process-recommendations-every-hour': {
        'task': 'your_django_app.tasks.process_recommendations',
        'schedule': crontab(hour='*', minute="5"),  # Adjust the timing as needed
    },
}
