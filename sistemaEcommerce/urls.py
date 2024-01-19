from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

schema_view  = get_schema_view(title="Sistema Ecommerce")
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')), 
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_schema/', schema_view,  name='api_schema' ),
    path('', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url':'api_schema'}), name='swagger-ui')
]

