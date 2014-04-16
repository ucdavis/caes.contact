from zope.interface import alsoProvides
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from rwproperty import getproperty, setproperty
from caes.contact import MessageFactory as _
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget


class IContact(form.Schema):
    """Marker/Form interface for contact behavior
    """
    contact = schema.Text(
        title=_(u'Contact Info'),
        required=False,
        )

    form.widget(contact='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')

alsoProvides(IContact, IFormFieldProvider)


class Contact(object):
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context

    @getproperty
    def contact(self):
        return getattr(self.context, 'contact', '')

    @setproperty
    def contact(self, value):
        setattr(self.context, 'contact', value)
