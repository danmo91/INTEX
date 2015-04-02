# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427935175.019823
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/orders.edit.html'
_template_uri = 'orders.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'foot_links']


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
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer(' <!-- foot_links -->\n')
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
        __M_writer('\n\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Order Details</h1>\n      </div>\n    </div>\n\n    <form method="POST">\n\t\t\t<table class="table table-striped table-bordered">\n\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\n\t\t\t</table>\n\t\t\t<button class="btn btn-primary pull-right save" type="submit">Save</button>\n\t\t</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/css/bootstrap-select.min.css">\n<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/js/bootstrap-select.min.js"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/orders.edit.html", "uri": "orders.edit.html", "source_encoding": "ascii", "line_map": {"80": 74, "74": 22, "68": 22, "53": 3, "47": 26, "42": 20, "27": 0, "60": 3, "61": 14, "62": 14, "37": 1}}
__M_END_METADATA
"""
