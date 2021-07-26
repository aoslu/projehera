from django.contrib import admin
from herapp.models import NargileKomuru, Photo,BriketKomur,PresSosisMangalKuru, NakliyeFoto,MeseKomur, Message, Urunler
# Register your models here.

admin.site.register(Photo)
admin.site.register(BriketKomur)
admin.site.register(PresSosisMangalKuru)
admin.site.register(NakliyeFoto)
admin.site.register(MeseKomur)
admin.site.register(NargileKomuru)

#admin.site.register(Message)



class MessageAdmin(admin.ModelAdmin):
    list_display= ('name',)
    search_fields= ('name',)

admin.site.register(Message, MessageAdmin)


admin.site.register(Urunler)