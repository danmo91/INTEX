# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427923671.243165
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/myaccount.html'
_template_uri = 'myaccount.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def center():
            return render_center(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n  <div class="panel panel-default">\n    <div class="panel-heading">\n      <h3 class="panel-title">My Account</h3>\n    </div>\n    <div class="panel-body">\n\n      <table class="table table-striped table-bordered">\n\n        <tr>\n          <th>Username</th>\n          <th>First Name</th>\n          <th>Last Name</th>\n          <th>Email</th>\n          <th>Phone</th>\n          <th>Actions</th>\n        </tr>\n\n\n          <tr>\n            <td>')
        __M_writer(str( user.username ))
        __M_writer('</td>\n            <td>')
        __M_writer(str( user.first_name ))
        __M_writer('</td>\n            <td>')
        __M_writer(str( user.last_name ))
        __M_writer('</td>\n            <td>')
        __M_writer(str( user.email ))
        __M_writer('</td>\n            <td>')
        __M_writer(str( user.phone ))
        __M_writer('</td>\n            <td>\n              <a id="edit_user_modal" href="#"> Edit </a>\n              |\n              <a id="change_password_modal" href="#"> Change Password </a>\n            </td>\n          </tr>\n      </table>\n\n    </div>\n    <div class="panel-footer">\n\n    </div>\n  </div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/myaccount.html", "source_encoding": "ascii", "uri": "myaccount.html", "line_map": {"35": 1, "69": 63, "40": 48, "46": 3, "59": 28, "53": 3, "54": 26, "55": 26, "56": 27, "57": 27, "58": 28, "27": 0, "60": 29, "61": 29, "62": 30, "63": 30}}
__M_END_METADATA
"""
