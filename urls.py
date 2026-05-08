"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_pages.views import SignUpView
urlpatterns = [
    # 1. Administración
    path('admin/', admin.site.urls),

    # 2. Mensajeria
    path('mensajes/', include('app_mensajeria.urls')),  # <-- Cerrar con ) y poner ,
    
    # 3. App principal (Reddit casero / LeoparX)
    path('', include('app_pages.urls')),               # <-- Cerrar con ) y poner ,
    
    # 4. Sistema de Usuarios (Login, Logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')), # <-- Cerrar con ) y poner ,
    
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # 5. Otras apps (Si las vas a usar para la entrega)
    path('coder/', include('AppCoder.urls')),          # <-- Cerrar con ) y poner ,
] 

# 5. Configuración para ver imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    