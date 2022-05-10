from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name="get_all_orders"),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name="get_order_by_id"),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name="update_order_status"),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name="get_orders_by_user"),
    path('user/<int:user_id>/orders/<int:order_id>/', views.UserOrderDetailView.as_view(), name="get_order_by_user_and_order_id")
]
