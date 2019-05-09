from django.contrib import admin

from import_export import resources
from .models import Questionnaire
from import_export.admin import ImportExportModelAdmin


class QuestionnaireResource(resources.ModelResource):

    class Meta:
        model = Questionnaire


class QuestionnaireAdmin(ImportExportModelAdmin):
    resource_class = QuestionnaireResource


# Register your models here.

admin.site.register(Questionnaire, QuestionnaireAdmin)
