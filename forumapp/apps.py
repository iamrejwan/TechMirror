from django.apps import AppConfig


class ForumappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forumapp'

    def ready(self):
        import forumapp.signals