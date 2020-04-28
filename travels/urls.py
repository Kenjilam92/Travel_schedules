from django.urls import path
from . import views
urlpatterns=[
    path ('',views.dashboard),
    path ('add',views.add_plan),
    path ('adding',views.adding_plan),
    path ('destination/<id>',views.plan_details),
    path ('join/<id>',views.join_plan),
]