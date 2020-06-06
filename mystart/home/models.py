from django.db import models

from wagtail.core.models import Page
<<<<<<< HEAD


class HomePage(Page):
    pass
=======
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]


>>>>>>> 64b6e3957d1e08872bd629ae2083cd4d763c2798
