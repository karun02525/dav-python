from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="DAV API",
      default_version='v1',
      description="For school description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('students.urls')),
                  path('api/', include('appadmin.urls')),
                  path('api/', include('teacher.urls')),
                  path('api/', include('authentication.urls')),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('', include('website.urls')),
                  path('api/', include('attendance.urls')),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
