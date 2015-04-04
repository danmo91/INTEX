# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428170900.329028
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/homepage/templates/recover_password_email.html'
_template_uri = 'recover_password_email.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        activation_link = context.get('activation_link', UNDEFINED)
        temp_password = context.get('temp_password', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\n    <head>\n        <title>Password Recovery</title>\n    </head>\n    <body>\n\n        Click this link within 24 hours to reset your password\n        <a href="')
        __M_writer(str( activation_link ))
        __M_writer('">Reset Password</a>\n\n        Temporary Password: ')
        __M_writer(str( temp_password ))
        __M_writer('\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/homepage/templates/recover_password_email.html", "line_map": {"16": 0, "33": 27, "23": 1, "24": 8, "25": 8, "26": 10, "27": 10}, "uri": "recover_password_email.html"}
__M_END_METADATA
"""
