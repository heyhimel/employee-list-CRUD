from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('add-employee/', addEmployee, name='add-employee'),
    path('employees/', employees, name="employeesData"),
    path('deleteEmployee/<int:empID>', delEmployee, name='delete-employee'),
    path('edit-employee/<int:empID>', editEmployee, name='edit-employee')
]
# we are in development server, that's why we are using static url for image media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
