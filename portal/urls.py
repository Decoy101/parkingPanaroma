
from django.urls import include, path

from . import AdminViews, views

urlpatterns = [
    path('',views.loginPage, name='login'),
    path('doLogin',views.doLogin,name="doLogin"),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('adminHomePage',AdminViews.Admin_HomePage,name="admin_home"),
    path('add_staff',AdminViews.add_staff,name="add_staff"),
    path('add_staff_save',AdminViews.add_staff_save,name="add_staff_save"),
    path('manage_staff',AdminViews.manage_staff,name="manage_staff"),
    path('delete_staff/<staff_id>',AdminViews.delete_staff,name="delete_staff"),
    path('edit_staff/<staff_id>/', AdminViews.edit_staff, name="edit_staff"),
    path('edit_staff_save', AdminViews.edit_staff_save, name="edit_staff_save"),
    path('new_entry',AdminViews.new_entry,name='new_entry'),
    path('new_entry_save',AdminViews.new_entry_save,name='new_entry_save'),
    path('delete_entry/<entry_id>',AdminViews.delete_entry,name='delete_entry'),
    path('add_parking',AdminViews.add_parking,name='add_parking'),
    path('add_parking_save',AdminViews.add_parking_save,name='add_parking_save'),
    path('delete_parking/<parking_id>',AdminViews.delete_parking,name='delete_parking'),
    path('dashboard',AdminViews.ReservationsListView.as_view(), name='dashboard'),
    path('parking',AdminViews.ParkingListView.as_view(),name='parking'),
    path('customer_details/<int:reservation_id>',AdminViews.customer_view,name='customer_details'),    
    path('update_parking',AdminViews.update_parking,name='update_parking'),
    path('update_status',AdminViews.update_status, name='update_status'),
    
]
