# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428348407.362438
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/INTEX/manager/templates/events.edit.html'
_template_uri = 'events.edit.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="jumbotron">\n    <div class="container">\n      <h1>Event Details</h1>\n    </div>\n  </div>\n\n\n  <form method="POST">\n\n    <table class="table table-striped table-bordered">\n\n      ')
        __M_writer(str( form ))
        __M_writer('\n\n    </table>\n    <button class="btn btn-primary pull-right save" type="submit">Save</button>\n\n  </form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.edit.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/INTEX/manager/templates/events.edit.html", "source_encoding": "ascii", "line_map": {"35": 1, "53": 3, "54": 16, "55": 16, "40": 23, "27": 0, "61": 55, "46": 3}}
__M_END_METADATA
"""
