from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.players import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"players", views.PlayerViewSet, basename="player")


app_name = "api"
urlpatterns = router.urls
