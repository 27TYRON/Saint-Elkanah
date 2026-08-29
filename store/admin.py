from django.contrib import admin
from .models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'size',
        'is_featured'
    )

    list_filter = (
        'is_featured',
    )

    search_fields = (
        'name',
    )