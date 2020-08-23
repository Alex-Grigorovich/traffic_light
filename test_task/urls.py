from django.urls import path

from test_task.views import upload_data, index

urlpatterns = [
    path('upload_data/', upload_data, name='upload_data'),
    path('', index, name='index'),

]
