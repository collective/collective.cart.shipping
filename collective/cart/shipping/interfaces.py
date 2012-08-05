from collective.cart.shipping import _
from zope import schema
from zope.interface import Attribute
from zope.interface import Interface


class IShippingMethod(Interface):

    to_country = schema.Choice(
        title=_(u"Country To"),
        required=False,
        description=_(u"Select countries to which this shipping method is applied."),
        vocabulary=_(u"Countries"))

    min_delivery_days = schema.Int(
        title=_(u"Minimum Delivery Days"),
        required=True)

    max_delivery_days = schema.Int(
        title=_(u"Maximum Delivery Days"),
        required=True)

    weight_dimension_rate = schema.Float(
        title=_(u"Weight Dimension Rate"),
        description=_(u"1 m3 = ??? kg"),
        required=False)

    vat = schema.Choice(
        title=_(u'VAT'),
        vocabulary=u'collective.behavior.vat.vats')


class ICartShippingMethod(Interface):

    title = Attribute(u'Title')
    orig_uuid = Attribute(u'Original UUID')
    min_delivery_days = Attribute(u"Minimum Delivery Days")
    max_delivery_days = Attribute(u"Maximum Delivery Days")
    gross = Attribute(u'Gross Fee')
    net = Attribute(u'Net Fee')
    vat = Attribute(u'VAT Fee')
