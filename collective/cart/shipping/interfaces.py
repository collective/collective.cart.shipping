from collective.cart.shipping import _
from zope import schema
from zope.interface import Interface


class IShippingMethod(Interface):

    from_country = schema.Choice(
        title=_(u"Country From"),
        required=False,
        description=_(u"Select countries from which this shipping method is applied."),
        vocabulary=_(u"Countries"),
    )

    to_country = schema.Choice(
        title=_(u"Country To"),
        required=False,
        description=_(u"Select countries to which this shipping method is applied."),
        vocabulary=_(u"Countries"),
    )

    min_delivery_days = schema.Int(
        title=_(u"Minimum Delivery Days"),
        required=True,
   )

    max_delivery_days = schema.Int(
        title=_(u"Maximum Delivery Days"),
        required=True,
   )

    dimension_weight_ratio = schema.Float(
        title=_(u"Dimention Weight Ratio"),
        description=_(u"1 m3 = ??? kg"),
        required=False,
   )