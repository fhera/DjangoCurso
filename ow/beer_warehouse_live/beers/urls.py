from os import path

from django.urls import path, re_path

from .views import (BeerDetailView, BeerListView, CompanyUpdateView,
                    CompanyDetailView, CompanyListView, CompanyCreateView)

urlpatterns = [
    path('list/', BeerListView.as_view(), name='beer-list-view'),
    re_path(
        r'^detail/(?P<pk>\d+)$',
        BeerDetailView.as_view(),
        name='beer-detail-view'
    ),

    re_path(
        r'^company/create/$',
        CompanyCreateView.as_view(),
        name='company-create-view'
    ),
    re_path(
        r'company/edit/(?P<pk>\d+)',
        CompanyUpdateView.as_view(),
        name='company-edit-view'
    ),
    re_path(
        r'^company/detail/(?P<pk>\d+)$',
        CompanyDetailView.as_view(),
        name='company-detail-view'
    ),
    re_path(
        r'^company/list/$',
        CompanyListView.as_view(),
        name='company-list-view'
    ),
]

# path('list/', beer_list_view, name='beer-list-view'),
# path('list-alt/', BeerListView.as_view(), name='beer-list-alt-view'),
# re_path(r'detail/(?P<pk>\d+)', beer_detail_view, name='beer-detail-view'),
