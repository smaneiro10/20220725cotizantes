from django.urls import path, include
from cotizantes import views

app_name='cotizantes'
urlpatterns = [
    path('', views.CotizantesListView.as_view(), name='cotizantes-list'),
    path('add/', views.CotizantesCreateView.as_view(), name='cotizantes-add'),
    path('<int:pk>/detail', views.CotizantesDetailView.as_view(), name='cotizantes-detail'),
    path('<int:pk>/detail1', views.CotizantesDetailView1.as_view(), name='cotizantes-detail1'),
    path('<int:pk>/update', views.CotizantesUpdateView.as_view(), name='cotizantes-update'),
    path('<int:pk>/delete', views.CotizantesDeleteView.as_view(), name='cotizantes-delete'),
]
