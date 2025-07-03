from django.urls import path
from . import views


urlpatterns = [
    #event-crud
    path('',views.event_list,name='event_list')
    path('events/<link:pk>/'views.event_detail,name='event_detail')
    path('events/create/',views.event_create,name='event_create')
    path('events/<link:pk>/update/',views.event_update,name='event_update')
    path('events/<link:pk>/delete/',views.event_delete,name='event_delete')
    
    
    #participant-crud
    path('participants/',views.participant_list,name='participant_list')
    path('participants/create/',views.participant_create,name='participant_create')
    path('participants/<link:pk>/update/',views.participant_update,name='participant_update')
    path('participants/<link:pk>/delete/',views.participant_delete,name='participant_delete')
    
    # categories
    
    path('categories/',views.category_list,name='category_list')
    path('categories/create/',views.category_create,name='category_create')
    path('categories/<link:pk>/update/',views.category_update,name='category_update')
    path('categories/<link:pk>/delete/',views.category_delete,name='category_delete')
    
    #dashboard
    
    path('dashboard/',views.dashboard,name='dashboard'),

]
