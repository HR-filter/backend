from django.urls import include, path

from rest_framework import routers

from .views import (
    StudentUserViewSet,
    PublicUserViewSet,
    FilterOptionsViewSet,
    FilterBooleanOpitionViewSet,
)
from docs.views import schema_view

app_name = "api"

# Роутер для API версии 1
router_v1 = routers.DefaultRouter()
router_v1.register("resume", StudentUserViewSet, "test")
router_v1.register("users", PublicUserViewSet, "users")
router_v1.register(r"filters", FilterOptionsViewSet, "filters")
router_v1.register(r"boolean-filters", FilterBooleanOpitionViewSet, "boolean")


urlpatterns = (
    path("", include(router_v1.urls)),
    path("auth/", include("djoser.urls.authtoken")),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
)
