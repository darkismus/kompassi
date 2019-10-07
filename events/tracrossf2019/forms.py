from django import forms

from core.utils import horizontal_form_helper
from enrollment.models import Enrollment


class EnrollmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        self.helper = horizontal_form_helper()

        self.fields['is_public'].required = True
        self.initial['is_public'] = True

    class Meta:
        model = Enrollment
        fields = (
            'is_public',
            'special_diet',
            'special_diet_other',
        )

        widgets = dict(
            special_diet=forms.CheckboxSelectMultiple,
        )
