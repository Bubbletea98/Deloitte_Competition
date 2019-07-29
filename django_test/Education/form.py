from django import forms
from crispy_forms.helper import FormHelper
from  django.core.validators import MaxValueValidator, MinValueValidator
from crispy_forms.layout import Layout, ButtonHolder, Submit
class NameForm(forms.Form):
    name = forms.CharField(
        label = "姓名",
        max_length = 80,
        required = True,
    )



    class Meta :
        fields =['name']


class LearningForm(forms.Form):

	name = forms.CharField(
        label = "知识点名称",
        max_length = 80,
        required = True,
    )

	score = forms.BooleanField(
        label = "是否正确",
        required = False,
    )

	difficulty = forms.IntegerField(
    	validators=[MinValueValidator(0),MaxValueValidator(10)],
        label = "难度（1-10）",
        required = True,
    )
	class Meta :
		fields =['name', 'score', 'difficulty']
