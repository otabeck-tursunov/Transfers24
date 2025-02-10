from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('latest-transfers/', TransfersView.as_view(), name='latest-transfers'),
    path('clubs/<int:pk>/info/', ClubInfoView.as_view(), name='club-info'),
    path('accurate/', Accurate150View.as_view(), name='accurate'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
