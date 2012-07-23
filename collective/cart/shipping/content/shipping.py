from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATCountryWidget.Widget import MultiCountryWidget
from Products.Archetypes.public import ATFieldProperty
from Products.Archetypes.public import AnnotationStorage
from Products.Archetypes.public import DecimalWidget
from Products.Archetypes.public import FloatField
from Products.Archetypes.public import IntegerField
from Products.Archetypes.public import IntegerWidget
from Products.Archetypes.public import LinesField
from Products.Archetypes.public import MultiSelectionWidget
from Products.Archetypes.public import Schema
from Products.Archetypes.public import TextAreaWidget
from Products.Archetypes.public import registerType
from Products.CMFCore.permissions import ModifyPortalContent
from Products.PythonField import PythonField
from collective.cart.shipping import PROJECTNAME
from collective.cart.shipping import _
from collective.cart.shipping.interfaces import IShippingMethod
from persistent import Persistent
from zope.interface import implements


default_script = """
## Python Script
##bind container=container
##bind context=context
##bind subpath=traverse_subpath
##parameters=article, request
##title=
##

# Available parameters:
#  request = The current HTTP request.
#            Access fields by request.form["myfieldname"]
#  article = collective.cart.core.Article object
#
# Return value is not processed -- unless you
# return a dictionary with contents. That's regarded
# as an error and will stop processing of actions
# and return the user to the form. Error dictionaries
# should be of the form {'field_id':'Error message'}

def shipping_fee(weight):
    return weight


return shipping_fee

"""


ShippingMethodSchema = ATContentTypeSchema.copy() + Schema((

    LinesField(
        name='to_country',
        required=False,
        searchable=False,
        languageIndependent=True,
        storage=AnnotationStorage(),
        widget=MultiCountryWidget(
            label=_(u'To Country'),
            description=_(u'Select countries to which this shipping method is applied.'),
            omitCountries=None)),

   IntegerField(
        name='min_delivery_days',
        required=True,
        searchable=False,
        languageIndependent=True,
        storage=AnnotationStorage(),
        widget=IntegerWidget(
            label=_(u'Minimum Delivery Days'),
            size='2',
            maxlength='2')),

   IntegerField(
        name='max_delivery_days',
        required=True,
        searchable=False,
        languageIndependent=True,
        storage=AnnotationStorage(),
        widget=IntegerWidget(
            label=_(u'Maximum Delivery Days'),
            size='2',
            maxlength='2')),

   FloatField(
        name='weight_dimension_rate',
        required=True,
        searchable=False,
        languageIndependent=True,
        storage=AnnotationStorage(),
        widget=DecimalWidget(
            label=_(u'Weight Dimension Rate'),
            description=_(u'1 m3 = ??? kg')),
        default=250.0),

    PythonField(
        name='shipping_fee',
        searchable=False,
        required=False,
        default=default_script,
        # read_permission=ModifyPortalContent,
        # write_permission=ModifyPortalContent,
        widget=TextAreaWidget(
            label=_(u'Shipping Fee Script'),
            rows=10,
            description = _(u'Script for calculationg shipping fee.')))))


finalizeATCTSchema(ShippingMethodSchema, folderish=False, moveDiscussion=False)


class ShippingMethod(ATCTContent):

    implements(IShippingMethod)

    portal_type = "ShippingMethod"
    _at_rename_after_creation = True

    schema = ShippingMethodSchema

    to_country = ATFieldProperty('to_country')
    min_delivery_days = ATFieldProperty('min_delivery_days')
    max_delivery_days = ATFieldProperty('max_delivery_days')
    weight_dimension_rate = ATFieldProperty('weight_dimension_rate')


registerType(ShippingMethod, PROJECTNAME)
