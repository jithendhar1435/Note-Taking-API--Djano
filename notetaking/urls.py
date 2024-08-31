from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView
schema_view = get_schema_view(
   openapi.Info(
      title="Note Taking API",
      default_version='v1',
      description="A simple API for note-taking",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@notetaking.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
