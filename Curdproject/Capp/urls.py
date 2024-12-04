from django.urls import path
from django.contrib import admin
from Capp import views

from.import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
]