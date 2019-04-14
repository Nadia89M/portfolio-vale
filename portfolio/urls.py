from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('<int:portfolio_id>', views.project, name='project'),
]