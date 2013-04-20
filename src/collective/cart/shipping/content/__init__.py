from collective.cart.shipping.interfaces import IShippingMethodContainer
from collective.cart.shipping.interfaces import IOrderShippingMethod
from plone.dexterity.content import Container
from zope.interface import implements


class ShippingMethodContainer(Container):
    """Content type: collective.cart.shopping.ShippingMethodContainer"""
    implements(IShippingMethodContainer)


class OrderShippingMethod(Container):
    """Content type: collective.cart.shopping.OrderShippingMethod"""
    implements(IOrderShippingMethod)

    title = None
    min_delivery_days = None
    max_delivery_days = None
    gross = None
    net = None
    vat = None
    vat_rate = None
    weight_dimension_rate = None
