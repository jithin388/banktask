from django import forms
from .models import details


# class detailForm(forms.ModelForm):
#     Materials=(
#         ("debitcard","debitcard"),
#         ("creditcard","creditcard"),
#         ("prepaidcard","prepaidcard"),
#         ("cheque","cheque"))
#     Materials= forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=Materials
#     )
  
#     class Meta:
#         model=details
#         fields=['materials']
        
    #     fields=['username','name','email','phone','gender','address','dob','district','branch','material']
    # def clean(self) :
        
    #     return super(detailForm).clean()
    

        