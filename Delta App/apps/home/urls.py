# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    
    path('', views.index, name='home'),
    path('page_index', views.page_index, name='page_index'),
    path('dataset',views.all_data,name='all_data'),
    path('import_data',views.import_data,name='import_data'),
    path('importer',views.importer,name='importer'),
    path('classifier',views.classifier,name='classifier'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    

]
