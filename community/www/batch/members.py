import frappe
from . import utils

def get_context(context):
    utils.get_common_context(context)
    if not context.membership:
        utils.redirect_to_lesson(context.course)
