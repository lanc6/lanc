from django.contrib import admin
from django.urls import path, include
from django.conf import settings                         # 추가 1
from django.conf.urls.static import static
from prj.views import HomeView
from prj.views import login
from prj.views import register

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('^login/', login.as_view(), name='login'),
    path('^register/', register.as_view(), name='register'),
    path('^UserCreateView/', register.as_view(), name='UserCreateView'),
    path('^UserCreateDoneTV/', register.as_view(), name='UserCreateDoneTV'),
    path(r'^accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('pizzas/', include('pizzas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:                                       # 추가 2
    import debug_toolbar                                 # 추가 2
    urlpatterns += [                                     # 추가 2
        path('__debug__/', include(debug_toolbar.urls)), # 추가 2
    ]                                                    # 추가 2
