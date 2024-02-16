from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('certchecker/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certchecker/add/', views.CertificateEditView.as_view(), name='certificate_add'),
    path('certchecker/<int:pk>/', views.CertificateView.as_view(), name='certificate'),
    path('certchecker/<int:pk>/edit/', views.CertificateEditView.as_view(), name='certificate_edit'),
    path('certchecker/<int:pk>/delete/', views.CertificateDeleteView.as_view(), name='certificate_delete'),
    path('certchecker-lists/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_changelog', kwargs={
        'model': models.Certificate
    }),
)
