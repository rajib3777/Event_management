from django.contrib import admin
from .models import Event,Participant,Category


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','date','location','status','category')
    list_filter = ('status','category')
    search_fields = ('name','location')
    prepopulated_fields={'slug' : ('name',)}
    filter_horizontal = ('participants',)
    
    
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')
    search_fields = ('name','email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description_short')
    
    def description_short(self,obj):
        return obj.description[:50] +'...' if obj.description else ''
    
    description_short.short_description = 'Description'