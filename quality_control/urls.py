from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    #path('bugs/', views.bug_list, name='bugs'),
    path('bugs/', views.bugs_list, name='bugs_list'),
    #path('requests/', views.features, name='reqs'),
    path('requests/', views.features_list, name='features_list'),
    #path('bugs/<int:bug_id>/', views.bug_detail),
    #path('bugs/<int:bug_id>/', views.bug_detail_from_all_bugs),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    #path('requests/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail')
    path('requests/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail')
]