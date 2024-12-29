from django.contrib import admin  # type: ignore # For Django's admin interface
from django.urls import path, include  # type: ignore # For including app-specific URLs
from rest_framework import routers, permissions  # type: ignore # For REST framework functionality
from drf_yasg.views import get_schema_view  # type: ignore # For generating Swagger UI
from drf_yasg import openapi  # type: ignore # For OpenAPI schema definitions
from apps.demo import views  # Import views from the demo app

# Swagger schema view configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',
        description="API for listing posts and fetching post details, including comments",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Router setup (can be used for ViewSets if applicable in the future)
router = routers.DefaultRouter()
# Uncomment the following line if you have a viewset for posts:
# router.register(r'posts', views.PostViewSet)

# URL patterns for the project
urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # API endpoints for posts and comments
    path('api/', include('apps.demo.urls')),

    # Swagger UI for API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Router URLs (if ViewSets are added in the future)
    # path('api/', include(router.urls)),
]
