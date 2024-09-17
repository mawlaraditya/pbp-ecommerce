from django.forms import ModelForm
from main.models import Hat

class AddNewHatForm(ModelForm):
    class Meta:
        model = Hat
        fields = ["name", "desc", "price"]