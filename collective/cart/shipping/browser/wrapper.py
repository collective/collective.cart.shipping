from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.cart.shipping.browser.form import ShippingMethodForm
from five import grok
from plone.z3cform.layout import FormWrapper


grok.templatedir('viewlets')


class ShippingMethodFormWrapper(FormWrapper):

    form = ShippingMethodForm
    index = ViewPageTemplateFile("viewlets/formwrapper.pt")
