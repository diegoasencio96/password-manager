from django.contrib import admin
from .models import Category, AccessCredential

# Register your models here.


@admin.register(AccessCredential)
class AccessCredentialAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'username', 'password', 'email', 'pin')
    readonly_fields = ('created_at', 'updated_at',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AccessCredentialAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)