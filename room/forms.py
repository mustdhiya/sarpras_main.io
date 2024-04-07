# File: sarpras_main/forms.py

from django import forms
from .models import RuangPercobaan

class RuangPercobaanForm(forms.ModelForm):
    class Meta:
        model = RuangPercobaan
        fields = ['nama', 'gedung', 'lantai', 'ket', 'svg_text']
