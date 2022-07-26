from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item, List

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


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

    def save(self, for_list: List):  # type: ignore
        # custom save method to allow saving of forms
        self.instance.list = for_list  # give form the list value
        return super().save()


class ExistingListItemForm(ItemForm):
    def __init__(self, for_list: List, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self) -> None:
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            # take the validation error, adjust its error message,
            # and then pass it back into the form
            e.error_dict = {"text": [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):  # type: ignore
        return forms.models.ModelForm.save(self)
