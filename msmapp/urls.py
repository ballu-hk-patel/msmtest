from django.urls import path
from .views import render_pdf_view,CustomerListView,customer_render

app_name="msmapp"

urlpatterns=[
    path("main_pdf/",CustomerListView.as_view(),name='main_view'),
    # path("pdf/",render_pdf_view,name='test_view'),
    path("pdf1/",customer_render,name='customer_render_view'),
]