# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427932964.671357
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/enter_payment.html'
_template_uri = 'enter_payment.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['foot_links', 'center']


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
        form = context.get('form', UNDEFINED)
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/js/bootstrap-select.min.js"></script>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container">\n\t<div class="row form-group">\n        <div class="col-xs-12">\n            <ul class="nav nav-pills nav-justified thumbnail setup-panel">\n                <li class="disabled"><a href="#step-1"\n                    <h4 class="list-group-item-heading">Step 1</h4>\n                    <p class="list-group-item-text">Confirm Order</p>\n                </a></li>\n                <li class="active"><a href="#step-2">\n                    <h4 class="list-group-item-heading">Step 2</h4>\n                    <p class="list-group-item-text">Enter Payment</p>\n                </a></li>\n                <li class="disabled"><a href="#step-3">\n                    <h4 class="list-group-item-heading">Step 3</h4>\n                    <p class="list-group-item-text">Third step description</p>\n                </a></li>\n            </ul>\n        </div>\n\t</div>\n</div>\n\n<div class="container">\n\n\t<div class="row">\n\n\t\t<form id="checkoutform" method="POST" action="/shop/receipt/">\n\t\t\t<div class="col-lg-4 col-lg-offset-4 col-md-8 col-sm-6 col-xs-12">\n\n\t\t\t\t<div class="form-group">\n\n')
        for field in form:
            __M_writer('\t\t\t\t\t\t')
            __M_writer(str( field ))
            __M_writer('\n')
        __M_writer('\n\t\t\t\t</div>\n\n\t\t\t\t<button class="btn btn-lg btn-primary btn-block" type="submit">Continue</button>\n\t\t\t</div>\n\t\t</form>\n\n\n\n\t</div>\n\n</div>\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 3, "27": 0, "37": 1, "72": 3, "73": 35, "42": 57, "75": 36, "76": 36, "77": 38, "47": 64, "83": 77, "53": 59, "59": 59, "74": 36}, "source_encoding": "ascii", "uri": "enter_payment.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/enter_payment.html"}
__M_END_METADATA
"""
