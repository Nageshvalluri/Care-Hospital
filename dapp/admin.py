
from django.contrib import admin
from .models import (
    CustomUser,
    Specialization,
    DoctorReg,
    PatientReg,
    Appointment,
    Page,
    AddPatient,
    MedicalHistory
)

# Optional: Customize display in admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    search_fields = ('username', 'email', 'first_name', 'last_name')

class DoctorRegAdmin(admin.ModelAdmin):
    list_display = ('admin', 'mobilenumber', 'fee', 'specialization_id')
    search_fields = ('admin__first_name', 'mobilenumber')

class PatientRegAdmin(admin.ModelAdmin):
    list_display = ('admin', 'mobilenumber', 'gender')
    search_fields = ('admin__first_name', 'mobilenumber')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointmentnumber', 'doctor_id', 'pat_id', 'date_of_appointment', 'status')
    list_filter = ('status', 'date_of_appointment')
    search_fields = ('pat_id__admin__first_name', 'doctor_id__admin__first_name')

class AddPatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor_id', 'mobilenumber', 'email')
    search_fields = ('name', 'mobilenumber')

class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('pat_id', 'bloodpressure', 'visitingdate_at')
    search_fields = ('pat_id__name',)



# Register all models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Specialization)
admin.site.register(DoctorReg, DoctorRegAdmin)
admin.site.register(PatientReg, PatientRegAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Page)
admin.site.register(AddPatient, AddPatientAdmin)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
