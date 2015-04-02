# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427925572.837965
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/myaccount.change_password.html'
_template_uri = 'myaccount.change_password.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <form class=form-signin id="change_password_form" method="POST" action="/shop/myaccount.change_password/">\n\n')
        for error in form.non_field_errors():
            __M_writer('\n        ')
            __M_writer(str( error ))
            __M_writer('\n\n')
        __M_writer('\n')
        for field in form:
            __M_writer('\n      <label class="sr-only"> ')
            __M_writer(str( field.name ))
            __M_writer('</label>\n\n      ')
            print('Field:',field) 
            
            __M_writer('\n\n        ')
            __M_writer(str( field ))
            __M_writer('\n\n')
            if field.errors != '':
                __M_writer('\n        ')
                __M_writer(str( field.errors ))
                __M_writer('\n\n')
            __M_writer('\n')
        __M_writer('\n    <button class="btn btn-lg btn-primary btn-block" type="submit">Save</button>\n\n  </form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/myaccount.change_password.html", "source_encoding": "ascii", "uri": "myaccount.change_password.html", "line_map": {"65": 17, "66": 19, "67": 19, "68": 21, "69": 22, "70": 23, "71": 23, "72": 26, "73": 28, "79": 73, "27": 0, "35": 1, "40": 34, "46": 3, "53": 3, "54": 7, "55": 8, "56": 9, "57": 9, "58": 12, "59": 13, "60": 14, "61": 15, "62": 15, "63": 17}}
__M_END_METADATA
"""
