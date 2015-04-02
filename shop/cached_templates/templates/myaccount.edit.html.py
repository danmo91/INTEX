# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427925570.612605
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/myaccount.edit.html'
_template_uri = 'myaccount.edit.html'
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
        __M_writer('\n\n\n<form class=form-signin id="editform" method="POST" action="/shop/myaccount.edit/">\n\n\n')
        for error in form.non_field_errors():
            __M_writer('\n      ')
            __M_writer(str( error ))
            __M_writer('\n\n')
        __M_writer('\n')
        for field in form:
            __M_writer('\n    <label class="sr-only"> ')
            __M_writer(str( field.name ))
            __M_writer('</label>\n\n      ')
            __M_writer(str( field ))
            __M_writer('\n\n')
            if field.errors != '':
                __M_writer('\n        ')
                __M_writer(str( field.errors ))
                __M_writer('\n\n')
            __M_writer('\n')
        __M_writer('\n  <button class="btn btn-lg btn-primary btn-block" type="submit">Save</button>\n\n</form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/myaccount.edit.html", "source_encoding": "ascii", "uri": "myaccount.edit.html", "line_map": {"64": 19, "65": 21, "66": 22, "67": 23, "68": 23, "69": 26, "70": 28, "76": 70, "27": 0, "35": 1, "40": 34, "46": 3, "53": 3, "54": 9, "55": 10, "56": 11, "57": 11, "58": 14, "59": 15, "60": 16, "61": 17, "62": 17, "63": 19}}
__M_END_METADATA
"""
