from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Factor)
admin.site.register(Cpu)
admin.site.register(Memory)
admin.site.register(Pci)
admin.site.register(BackPannel)
admin.site.register(Audio)
admin.site.register(Network)
admin.site.register(Memory_Types)
admin.site.register(Memory_Max_Sizes)
admin.site.register(Memory_Slots)
admin.site.register(Memory_Freq)
admin.site.register(Schema)