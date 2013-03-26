from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-collective.cart.shipping:default'


def reimport_registry(context, logger=None):
    """Reimport registry"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting registry.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'plone.app.registry', run_dependencies=False, purge_old=False)
