from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]


# class CategoryForm(ModelForm):
#     class Meta:
#         model = ExpenseCategory
#         fields = [
#             "name",
#         ]


# class AccountForm(ModelForm):
#     class Meta:
#         model = Account
#         fields = [
#             "name",
#             "number",
#         ]
