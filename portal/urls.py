
from django.urls import include, path

from . import AdminViews, views

urlpatterns = [
    # Admin URls
    path('',views.loginPage, name='login'),
    path('doLogin',views.doLogin,name="doLogin"),
    path('logout_user/',AdminViews.logout_user,name='logout_user'),
    path('adminHomePage',AdminViews.Admin_HomePage,name="admin_home"),
    path('add_staff',AdminViews.add_staff,name="add_staff"),
    path('add_staff_save',AdminViews.add_staff_save,name="add_staff_save"),
    path('manage_staff',AdminViews.manage_staff,name="manage_staff"),
    path('delete_staff/<staff_id>',AdminViews.delete_staff,name="delete_staff"),
    path('edit_staff/<staff_id>/', AdminViews.edit_staff, name="edit_staff"),
    path('edit_staff_save', AdminViews.edit_staff_save, name="edit_staff_save"),
    path('new_entry',AdminViews.new_entry,name='new_entry'),
    path('new_entry_save',AdminViews.new_entry_save,name='new_entry_save'),
    path('edit_entry/<entry_id>',AdminViews.edit_entry,name='edit_entry'),
    path('edit_entry_save/',AdminViews.edit_entry_save,name='edit_entry_save'),
    path('delete_entry/<entry_id>',AdminViews.delete_entry,name='delete_entry'),
    path('add_parking',AdminViews.add_parking,name='add_parking'),
    path('add_parking_save',AdminViews.add_parking_save,name='add_parking_save'),
    path('edit_parking/<parking_id>/',AdminViews.edit_parking,name='edit_parking'),
    path('edit_parking_save',AdminViews.edit_parking_save,name='edit_parking_save'),
    path('delete_parking/<parking_id>',AdminViews.delete_parking,name='delete_parking'),
    path('dashboard',AdminViews.ReservationListView, name='dashboard'),
    path('parking',AdminViews.ParkingListView,name='parking'),
    path('customer_details/<int:reservation_id>',AdminViews.customer_view,name='customer_details'),    
    path('update_status',AdminViews.update_status, name='update_status'),
    path('test-view/<customer_id>',AdminViews.render_pdf_view, name='test-view'),
    path('pdf',AdminViews.pdf,name='pdf')

    # Staff URls
    # path('',views.loginPage, name='login'),
    # path('doLogin',views.doLogin,name="doLogin"),
    # path('logout_user/',views.logout_user,name='logout_user'),
    # path('staffHomePage',StaffViews.Admin_HomePage,name="staff_home"),
    # path('new_entry',AdminViews.new_entry,name='staff_new_entry'),
    # path('new_entry_save',AdminViews.new_entry_save,name='new_entry_save'),
    # path('edit_entry/<entry_id>',AdminViews.edit_entry,name='staff_edit_entry'),
    # path('edit_entry_save/',AdminViews.edit_entry_save,name='edit_entry_save'),
    # path('delete_entry/<entry_id>',AdminViews.delete_entry,name='delete_entry'),
    # path('dashboard',AdminViews.ReservationsListView.as_view(), name='staff_dashboard'),
    # path('parking_staff',StaffViews.ParkingListView,name='staff_parking'),
    # path('customer_details/<int:reservation_id>',AdminViews.customer_view,name='customer_details'),    
    # path('update_parking',AdminViews.update_parking,name='update_parking'),
    # path('update_status',AdminViews.update_status, name='update_status'),
    
]
