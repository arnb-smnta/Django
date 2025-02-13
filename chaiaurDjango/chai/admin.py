from django.contrib import admin
from .models import ChaiVariety, chaiCertificate, store, review
# Register your models here.


class chaiReviewInline(admin.TabularInline):
    model = review
    extra = 2


class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
    inlines = [chaiReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("ChaiVariety",)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number")


admin.site.register(ChaiVariety, chaiVarietyAdmin)
admin.site.register(store, StoreAdmin)
admin.site.register(chaiCertificate, ChaiCertificateAdmin)
