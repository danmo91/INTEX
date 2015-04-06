# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428348438.605727
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/INTEX/manager/templates/rentals.overdue.html'
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
        over_30 = context.get('over_30', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        over_90 = context.get('over_90', UNDEFINED)
        over_60 = context.get('over_60', UNDEFINED)
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
        over_30 = context.get('over_30', UNDEFINED)
        def content():
            return render_content(context)
        over_90 = context.get('over_90', UNDEFINED)
        over_60 = context.get('over_60', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <h2>Over 30</h2>\n\n  <table class="table table-striped">\n\n    <thead>\n      <th>Rental</th>\n      <th>Due Date</th>\n    </thead>\n\n    <tbody>\n\n')
        for r in over_30:
            __M_writer('\n        <tr>\n\n          <td>')
            __M_writer(str( r.description ))
            __M_writer('</td>\n          <td>')
            __M_writer(str( r.due_date ))
            __M_writer('</td>\n\n        </tr>\n\n')
        __M_writer('\n    </tbody>\n\n    <tfoot>\n      <td></td>\n      <td></td>\n      <td></td>\n    </tfoot>\n\n  </table>\n\n  <h2>Over 60</h2>\n\n  <table class="table table-striped">\n\n    <thead>\n      <th>Rental</th>\n      <th>Due Date</th>\n    </thead>\n\n    <tbody>\n\n')
        for r in over_60:
            __M_writer('\n        <tr>\n\n          <td>')
            __M_writer(str( r.description ))
            __M_writer('</td>\n          <td>')
            __M_writer(str( r.due_date ))
            __M_writer('</td>\n\n        </tr>\n\n')
        __M_writer('\n    </tbody>\n\n    <tfoot>\n      <td></td>\n      <td></td>\n      <td></td>\n    </tfoot>\n\n  </table>\n\n  <h2>Over 90</h2>\n\n  <table class="table table-striped">\n\n    <thead>\n      <th>Rental</th>\n      <th>Due Date</th>\n    </thead>\n\n    <tbody>\n\n')
        for r in over_90:
            __M_writer('\n        <tr>\n\n          <td>')
            __M_writer(str( r.description ))
            __M_writer('</td>\n          <td>')
            __M_writer(str( r.due_date ))
            __M_writer('</td>\n\n        </tr>\n\n')
        __M_writer('\n    </tbody>\n\n    <tfoot>\n      <td></td>\n      <td></td>\n      <td></td>\n    </tfoot>\n\n  </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentals.overdue.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/INTEX/manager/templates/rentals.overdue.html", "source_encoding": "ascii", "line_map": {"64": 26, "65": 48, "66": 49, "67": 52, "68": 52, "69": 53, "70": 53, "71": 58, "72": 80, "73": 81, "74": 84, "75": 84, "76": 85, "77": 85, "78": 90, "84": 78, "27": 0, "37": 1, "42": 101, "48": 3, "57": 3, "58": 16, "59": 17, "60": 20, "61": 20, "62": 21, "63": 21}}
__M_END_METADATA
"""
