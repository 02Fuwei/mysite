from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInIine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["question_text"]}),
        ("Date information",{"fields":["pub_date"],"classes":["collapse"]})
    ]
    inlines = [ChoiceInIine]
    list_display = ["question_text","pub_date","was_published_recently"] # 排序
    list_filter = ["pub_date"] #侧边栏 过滤器
    search_fields = ["question_text"]  #搜索框
admin.site.register(Question,QuestionAdmin)
