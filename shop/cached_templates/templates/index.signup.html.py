# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427923761.913536
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/index.signup.html'
_template_uri = 'index.signup.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <!-- <form id="signup_form" method="POST" action="/shop/index.signup/">\n\n  <table>\n    ')
        __M_writer(str( form ))
        __M_writer('\n  </table>\n\n  <input type="submit" class="btn btn-success"/>\n</form> -->\n\n\n\n\n\n<form class=form-signin id="signup_form" method="POST" action="/shop/index.signup/">\n\n\n')
        for error in form.non_field_errors():
            __M_writer('\n      ')
            __M_writer(str( error ))
            __M_writer('\n\n')
        __M_writer('\n')
        for field in form:
            __M_writer('\n    <label class="sr-only"> ')
            __M_writer(str( field.name ))
            __M_writer('</label>\n\n\n\n      ')
            __M_writer(str( field ))
            __M_writer('\n\n')
            if field.errors != '':
                __M_writer('\n      ')
                __M_writer(str( field.errors ))
                __M_writer('\n\n')
            __M_writer('\n')
        __M_writer('\n  <button class="btn btn-lg btn-primary btn-block" type="submit">Signup</button>\n\n</form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/index.signup.html", "source_encoding": "ascii", "uri": "index.signup.html", "line_map": {"64": 29, "65": 33, "66": 33, "67": 35, "68": 36, "69": 37, "70": 37, "71": 40, "72": 42, "78": 72, "27": 0, "35": 1, "40": 48, "46": 3, "53": 3, "54": 8, "55": 8, "56": 21, "57": 22, "58": 23, "59": 23, "60": 26, "61": 27, "62": 28, "63": 29}}
__M_END_METADATA
"""
