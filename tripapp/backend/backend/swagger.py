from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Trip Planner API",
        default_version='v1',
        description="API documentation for the Trip Planner project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@tripplanner.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
