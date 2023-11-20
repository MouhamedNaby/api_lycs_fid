from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Lycs Fid",
      default_version='v1',
      description="Vue des Api Lycs_fid",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('par
    #parametre
    # path('parametres/', views.ParametreList.as_view()),
    # path('parametres/user/<int:id>/', views.ParametreByUser.as_view()),
    # path('profiles/<int:id>/', views.CompanyByIdAPIView.as_view()),

    # path('envoyer-message/', SendTwilioMessageView.as_view(), name='envoyer-message'),
    

    
    
    

       
    
]


# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

# urlpatterns = [
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
# ]