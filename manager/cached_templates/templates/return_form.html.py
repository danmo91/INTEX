# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428121988.048723
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return_form.html'
_template_uri = 'return_form.html'
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
        rental = context.get('rental', UNDEFINED)
        form = context.get('form', UNDEFINED)
        round = context.get('round', UNDEFINED)
        late_fee = context.get('late_fee', UNDEFINED)
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
        rental = context.get('rental', UNDEFINED)
        form = context.get('form', UNDEFINED)
        round = context.get('round', UNDEFINED)
        late_fee = context.get('late_fee', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n<form class=form-return id="returnform" method="POST" action="/manager/return.return_form/')
        __M_writer(str(rental.id))
        __M_writer('">\n\n')
        for error in form.non_field_errors():
            __M_writer('\n            ')
            __M_writer(str( error ))
            __M_writer('\n\n')
        __M_writer('\n')
        for field in form:
            __M_writer('\n            ')
            __M_writer(str( field.label ))
            __M_writer('\n\n            ')
            __M_writer(str( field ))
            __M_writer('\n\n')
            if field.errors != '':
                __M_writer('\n            ')
                __M_writer(str( field.errors ))
                __M_writer('\n\n')
            __M_writer('\n')
        __M_writer('\n        <h4>Late Fee: $')
        __M_writer(str( round(late_fee,2) ))
        __M_writer('</h4>\n\n\n\n    <button class="btn btn-lg btn-primary btn-block" type="submit">Return</button>\n\n</form>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return_form.html", "uri": "return_form.html", "line_map": {"64": 10, "65": 10, "66": 13, "67": 14, "68": 15, "69": 16, "70": 16, "71": 18, "72": 18, "73": 20, "74": 21, "75": 22, "76": 22, "77": 25, "78": 27, "79": 28, "80": 28, "86": 80, "27": 0, "38": 1, "43": 40, "49": 3, "59": 3, "60": 6, "61": 6, "62": 8, "63": 9}, "source_encoding": "ascii"}
__M_END_METADATA
"""
