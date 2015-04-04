# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428036812.326795
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return2.html'
_template_uri = 'return2.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'head_links', 'foot_links']


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
        def head_links():
            return render_head_links(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer('\n\n\n\n')
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
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="jumbotron">\n        <div class="container">\n            <h1>Rental Return</h1>\n        </div>\n    </div>\n\n    <div class="container">\n    <div class="row">\n        <div class="col-md-12">\n            <div class="well well-sm">\n                <form class="form-horizontal" method="post">\n                    <fieldset>\n                        <legend class="text-center header">Contact us</legend>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"><i class="fa fa-user bigicon"></i></span>\n                            <div class="col-md-8">\n                                <input id="fname" name="name" type="text" placeholder="First Name" class="form-control">\n                            </div>\n                        </div>\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"><i class="fa fa-user bigicon"></i></span>\n                            <div class="col-md-8">\n                                <input id="lname" name="name" type="text" placeholder="Last Name" class="form-control">\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"><i class="fa fa-envelope-o bigicon"></i></span>\n                            <div class="col-md-8">\n                                <input id="email" name="email" type="text" placeholder="Email Address" class="form-control">\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"><i class="fa fa-phone-square bigicon"></i></span>\n                            <div class="col-md-8">\n                                <input id="phone" name="phone" type="text" placeholder="Phone" class="form-control">\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"><i class="fa fa-pencil-square-o bigicon"></i></span>\n                            <div class="col-md-8">\n                                <textarea class="form-control" id="message" name="message" placeholder="Enter your massage for us here. We will get back to you within 2 business days." rows="7"></textarea>\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <div class="col-md-12 text-center">\n                                <button type="submit" class="btn btn-primary btn-lg">Submit</button>\n                            </div>\n                        </div>\n                    </fieldset>\n                </form>\n            </div>\n        </div>\n    </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/css/bootstrap-select.min.css">\n<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/js/bootstrap-select.min.js"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 10, "27": 0, "38": 1, "71": 4, "43": 6, "77": 4, "48": 72, "83": 74, "53": 79, "89": 74, "59": 10, "95": 89}, "source_encoding": "ascii", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return2.html", "uri": "return2.html"}
__M_END_METADATA
"""
