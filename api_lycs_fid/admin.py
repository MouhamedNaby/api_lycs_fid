from django.contrib import admin
from .models import*
from api_lycs_fid import*

class UserAdmin(admin.ModelAdmin):
    pass
class PartnerAdmin(admin.ModelAdmin):
    pass
class ClientAdmin(admin.ModelAdmin):
    pass
class BonAdmin(admin.ModelAdmin):
    pass
class ArticlAdmin(admin.ModelAdmin):
    pass
class CampagneAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Article, ArticlAdmin)
admin.site.register(BonReduction, BonAdmin)
admin.site.register(Campagne, CampagneAdmin)

