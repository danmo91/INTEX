# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428359544.189945
_enable_loop = True
_template_filename = 'C:\\Users\\brian_000\\projects\\intex\\events\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'meta', 'header', 'events', 'footer']


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
    return runtime._inherit_from(context, '/base/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def meta():
            return render_meta(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def events():
            return render_events(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'events'):
            context['self'].events(**pageargs)
        

        __M_writer(' <!-- homepage -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n<meta charset="UTF-8">\r\n<meta name="description" content="Colonial American Events in Provo, UT">\r\n<meta name="keywords" content="Colonial Utah America">\r\n<meta name="author" content="Dan Morain">\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <!-- Navbar -->\r\n    <nav class="navbar navbar-default navbar-fixed-top">\r\n          <div class="container-fluid">\r\n            <!-- Brand and toggle get grouped for better mobile display -->\r\n            <div class="navbar-header">\r\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                <span class="sr-only">Toggle navigation</span>\r\n                <span class="icon-bar"></span>\r\n                <span class="icon-bar"></span>\r\n                <span class="icon-bar"></span>\r\n              </button>\r\n              <a class="navbar-brand" href="/homepage/index/">Colonial Heritage Foundation</a>\r\n            </div>\r\n\r\n            <!-- Collect the nav links, forms, and other content for toggling -->\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n              <ul class="nav navbar-nav">\r\n                <li id="tab"><a href="#">About</a></li>\r\n                <li id="tab"><a href="#">Contact</a></li>\r\n                <li id="tab"><a href="/shop/index/">Shop</a></li>\r\n                <li id="tab"><a href="/events/index/">Events</a></li>\r\n\r\n')
        if request.user.is_staff:
            __M_writer('              <li class="dropdown">\r\n                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Admin <span class="caret"></span></a>\r\n                    <ul class="dropdown-menu" role="menu">\r\n                      <li><a href="/manager/events">Events</a></li>\r\n                      <li><a href="/manager/items">Items</a></li>\r\n                      <li><a href="/manager/products">Products</a></li>\r\n                      <li><a href="/manager/orders">Orders</a></li>\r\n                      <li><a href="/manager/rentals">Rentals</a></li>\r\n                      <li class="divider"></li>\r\n                      <li><a href="/manager/users">Users</a></li>\r\n                      <li class="divider"></li>\r\n                      <li><a href="/manager/return">Rental Return</a></li>\r\n                      <li><a id="show_overdue_rentals">See Overdue Rentals</a></li>\r\n                    </ul>\r\n                  </li>\r\n')
        __M_writer('\r\n\r\n              </ul>\r\n\r\n              <form class="navbar-form navbar-left" role="search">\r\n                <div class="form-group">\r\n                  <input type="text" class="form-control" placeholder="Search">\r\n                </div>\r\n                <button type="submit" class="btn btn-default">Submit</button>\r\n              </form>\r\n              <ul class="nav navbar-nav navbar-right">\r\n              </ul>\r\n            </div><!-- /.navbar-collapse -->\r\n          </div><!-- /.container-fluid -->\r\n        </nav>\r\n\r\n\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_events(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        def events():
            return render_events(context)
        def center():
            return render_center(context)
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer(' <!-- header -->\r\n\r\n\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer(' <!-- center -->\r\n\r\n\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer(' <!-- footer -->\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="footer">\r\n      <nav class="footer navbar navbar-fixed-bottom">\r\n      </nav>\r\n    </div>\r\n\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"65": 74, "27": 0, "133": 80, "71": 4, "145": 139, "112": 12, "122": 76, "43": 1, "77": 4, "48": 10, "99": 12, "91": 36, "83": 13, "139": 80, "53": 92, "127": 87, "90": 13, "59": 74, "92": 37, "93": 53, "117": 70}, "source_encoding": "ascii", "filename": "C:\\Users\\brian_000\\projects\\intex\\events\\templates/base.htm"}
__M_END_METADATA
"""
