from collective.cart.shipping import _
from plone.supermodel.model import Schema
from zope import schema


class ShippingMethodContainerSchema(Schema):
    """Schema for content type: collective.cart.shipping.ShippingMethodContainer"""


class ShippingMethodSchema(Schema):
    """Schema for content type: ShippingMethod"""

    to_country = schema.Choice(
        title=_(u"Country To"),
        required=False,
        description=_(u"Select countries to which this shipping method is applied."),
        vocabulary=_(u"Countries"))

    min_delivery_days = schema.Int(
        title=_(u"Minimum Delivery Days"),
        required=False)

    max_delivery_days = schema.Int(
        title=_(u"Maximum Delivery Days"),
        required=False)

    weight_dimension_rate = schema.Float(
        title=_(u"Weight Dimension Rate"),
        description=_(u"1 m3 = ??? kg"),
        required=False)

    vat = schema.Choice(
        title=_(u'VAT'),
        vocabulary=u'collective.behavior.vat.rates')


class OrderShippingMethodSchema(Schema):
    """Schema for content type: collective.cart.shipping.OrderShippingMethod"""
