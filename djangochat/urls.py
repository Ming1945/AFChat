from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import handler404

urlpatterns = [
    path('qwertzui/', admin.site.urls),
    path('', include('chat.urls'))
]

# handler404 = 'chat.views.error_404_view'