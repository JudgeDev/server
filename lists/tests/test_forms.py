from django.test import TestCase

from lists.forms import EMPTY_ITEM_ERROR, ItemForm


class ItemFormTest(TestCase):
    """Test form for item entry

    form = ItemForm()
    form.as_p())  # render form as html
    """

    def test_form_item_input_has_placeholder_and_css_classes(self) -> None:
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self) -> None:
        form = ItemForm(data={"text": ""})
        # check form validation before saving
        # is_valid() validates
        self.assertFalse(form.is_valid())
        # ...and populates errors attribute
        self.assertEqual(form.errors["text"], [EMPTY_ITEM_ERROR])
