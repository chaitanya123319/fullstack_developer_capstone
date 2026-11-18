from django.contrib import admin
from .models import Dealer, Review


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'state', 'phone')
    search_fields = ('name', 'city', 'state')
    list_filter = ('state',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'dealer', 'name', 'created_at')
    search_fields = ('name', 'review')