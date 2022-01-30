from django import forms
from .models import Review

# FORM WHICH USE STANDARD FORMS
# RESULT IS THE SAME OF BOTH OF THOSE CODES
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "please enter shorter name"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# OTHER PHILOSOPHY WHICH BASE ON ALREADY EXISTING FORMS ON MODELS.PY
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # optionally you can select ALL
        # exclude = ['']  # or you can exclude some fields from models
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "please enter shorter name"
            }
        }
