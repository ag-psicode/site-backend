from django.contrib import admin
from estimates.models import EstimateRequest, Question, QuestionChoice

class QuestionAdmin(admin.ModelAdmin):
    pass

class QuestionChoiceAdmin(admin.ModelAdmin):
    pass

class EstimateRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(EstimateRequest, EstimateRequestAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)