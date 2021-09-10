from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StudentListCreate.as_view()),
    path('<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]