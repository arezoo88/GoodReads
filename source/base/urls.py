from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.book.api.v1.urls', namespace='book.v1')),
    path('api/v1/', include('apps.account.api.v1.urls', namespace='account.v1')),

]
# This is only needed when using runserver.(debug is true)
if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view
    from rest_framework.permissions import AllowAny

    schema_view = get_schema_view(
        openapi.Info(
            title=f'{settings.SITE["NAME"]} APIs',
            default_version=f'{settings.REST_FRAMEWORK["DEFAULT_VERSION"]}',
            description=f'{settings.SITE["DESCRIPTION"]}',
            contact=openapi.Contact(email=f'{settings.DEFAULT_FROM_EMAIL}')
        ),
        public=True,
        permission_classes=(AllowAny,)
    )
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'),
        path('redoc', schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc')
    ]
