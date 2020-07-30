from django import forms
from mess import models
class msgform(forms.ModelForm):
    class Meta:
        model = models.messagerecord
        fields = ['msg_content',]