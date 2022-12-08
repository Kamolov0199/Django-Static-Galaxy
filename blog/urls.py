from django.contrib import admin
from django.urls import path
from core.views import main, AboutView, ContactView, PagesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('pages/', PagesView.as_view()),
]
