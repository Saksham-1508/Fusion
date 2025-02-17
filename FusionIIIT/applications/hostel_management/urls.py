from django.urls import path, include
from . import views

app_name = 'hostelmanagement'

urlpatterns = [
    #Home 
    path('', views.hostel_view, name="hostel_view"),

    #Notice Board
    path('notice_form/', views.notice_board, name="notice_board"),
    path('delete_notice/', views.delete_notice, name="delete_notice"),

    #Worker Schedule
    path('edit_schedule/', views.staff_edit_schedule, name='staff_edit_schedule'),
    path('delete_schedule/', views.staff_delete_schedule, name='staff_delete_schedule'),
    
    #Student Room
    path('edit_student/',views.edit_student_room,name="edit_student_room"),
    path('edit_student_rooms_sheet/', views.edit_student_rooms_sheet, name="edit_student_rooms_sheet"),
    path('insert_rooms/',views.insert_rooms,name="insert_rooms"),

    #Guest Room
    path('book_guest_room/', views.request_guest_room, name="book_guest_room"),
    path('update_guest_room/', views.update_guest_room, name="update_guest_room"),
    
    #Attendance
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),

    #Attendance
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),

    #Worker Report
    path('worker_report/', views.generate_worker_report, name='workerreport'),
    path('pdf/', views.GeneratePDF.as_view(), name="pdf"),

    #API endpoints
    path('api/', include('applications.hostel_management.api.urls'))
]