from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #path('', views.index),
    path('', views.IndexView.as_view(), name='index'),

    #path('bugs/', views.bugs_list, name='bugs_list'),
    path('bugs/', views.BugListView.as_view(), name='bugs_list'),

    #path('requests/', views.features_list, name='features_list'),
    path('requests/', views.FeatureListView.as_view(), name='features_list'),

    #path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),

    #path('requests/<int:feature_id>/', views.feature_detail, name='feature_detail')
    path('requests/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),

    path('bug/new/', views.create_bugreport, name='create_bugreport'),

    path('featurerequest/new/', views.create_featurerequest, name='create_featurerequest'),
]