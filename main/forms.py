from django.forms import ModelForm
from main.models import MoodEntry

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["product", "desc", "price", "stock", "image"]