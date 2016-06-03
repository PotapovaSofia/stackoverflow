# -*- coding: utf-8 -*-
from django import forms
from .models import Event

class QuesForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField()


class EventListForm(forms.Form):
	search = forms.CharField(required=False)
	sort_field = forms.ChoiceField(choices=(("id", "ID"), ('create_date', 'created')), required=False)

"""
class MyCoolForm(forms.Form): 
	title = forms.CharField()
	text = forms.CharField(label=u'Текст поста')
    is_published = forms.BooleanField(label=u'Опубликовать пост')
    def clean(self):
        data = super(MyCoolForm, self).clean()
        if data.get('is_published' and not data.get('text'):
            raise forms.ValidationError(u'Вы не можете опубликовать пост, пока не заполните его текстом')
        return data
"""
