from django import forms


class CompanyReviewForm(forms.Form):
    user = forms.CharField(label="User")
    review = forms.CharField(
        label="Accompanying text", max_length=800, widget=forms.Textarea, strip=True
    )
    likes = forms.BooleanField(label="Like")
    dislikes = forms.BooleanField(label="Dislikes")
