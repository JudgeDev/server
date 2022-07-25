from django import forms

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):
    """Form for item entry

    Could define the form manually:
    item_text = forms.CharField(   # text field
        widget=forms.fields.TextInput(attrs={  # customise form
            'placeholder': 'Enter a to-do item',
            'class': 'form-control input-lg',
        })
    )
    Better to reuse the validation code already defined for the model.
    Autogenerate a form for a model using ModelForm
    It assigns sensible html form input types to fields and
    applies default validation.
    """

    class Meta:
        # configure form
        model = Item  # specify the model
        fields = ("text",)  # specify fields to use
        widgets = {  # override the ModelForm fields
            "text": forms.fields.TextInput(
                attrs={
                    "placeholder": "Enter a to-do item",
                    "class": "form-control input-lg",
                }
            ),
        }
        error_messages = {  # customise default error message
            "text": {"required": EMPTY_ITEM_ERROR}
        }
