# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427250816.532454
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/rentals.overdue.html'
_template_uri = 'rentals.overdue.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <table class="table table-striped">\n\n    <thead>\n      <th>Rental</th>\n      <th>Rental Date</th>\n      <th>Due Date</th>\n    </thead>\n\n    <tbody>\n\n')
        for item in items:
            __M_writer('\n        <tr>\n\n          <td>')
            __M_writer(str( item.description ))
            __M_writer('</td>\n          <td>')
            __M_writer(str( item.rental_date ))
            __M_writer('</td>\n          <td>')
            __M_writer(str( item.due_date ))
            __M_writer('</td>\n\n        </tr>\n\n')
        __M_writer('\n    </tbody>\n\n    <tfoot>\n      <td></td>\n      <td></td>\n      <td></td>\n    </tfoot>\n\n  </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "rentals.overdue.html", "line_map": {"35": 1, "68": 62, "40": 37, "46": 3, "59": 20, "53": 3, "54": 15, "55": 16, "56": 19, "57": 19, "58": 20, "27": 0, "60": 21, "61": 21, "62": 26}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/rentals.overdue.html"}
__M_END_METADATA
"""
