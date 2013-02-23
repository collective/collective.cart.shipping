from Products.CMFCore.utils import getToolByName


def installProductsATCountryWidget(portal):
    installer = getToolByName(portal, 'portal_quickinstaller')
    installer.installProduct('Products.ATCountryWidget')


def setupVarious(context):

    if context.readDataFile('collective.cart.shipping_various.txt') is None:
        return

    portal = context.getSite()
    installProductsATCountryWidget(portal)
