# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427923459.060924
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['foot_links', 'header', 'center', 'admin', 'footer', 'head_links']


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
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def admin():
            return render_admin(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def head_links():
            return render_head_links(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!-- CSS/JS Links that belong only to the homepage app -->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer(' <!-- head_links -->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admin'):
            context['self'].admin(**pageargs)
        

        __M_writer(' <!-- admin -->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer(' <!-- foot_links -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- Navbar -->\n    <nav class="navbar navbar-default navbar-fixed-top">\n          <div class="container-fluid">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="/homepage/index/">Colonial Heritage Foundation</a>\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul class="nav navbar-nav">\n                <li id="tab"><a href="#">About</a></li>\n                <li id="tab"><a href="#">Contact</a></li>\n                <li id="tab"><a href="/shop/index/">Shop</a></li>\n\n')
        if request.user.is_staff:
            __M_writer('                  <li class="dropdown">\n                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Admin <span class="caret"></span></a>\n                    <ul class="dropdown-menu" role="menu">\n                      <li><a href="/manager/events">Events</a></li>\n                      <li><a href="/manager/items">Items</a></li>\n                      <li><a href="/manager/products">Products</a></li>\n                      <li><a href="/manager/orders">Orders</a></li>\n                      <li><a href="/manager/rentals">Rentals</a></li>\n                      <li class="divider"></li>\n                      <li><a href="/manager/users">Users</a></li>\n                      <li class="divider"></li>\n                      <li><a id="show_overdue_rentals">See Overdue Rentals</a></li>\n                    </ul>\n                  </li>\n')
        __M_writer('\n\n              </ul>\n\n              <form class="navbar-form navbar-left" role="search">\n                <div class="form-group">\n                  <input type="text" class="form-control" placeholder="Search">\n                </div>\n                <button type="submit" class="btn btn-default">Submit</button>\n              </form>\n              <ul class="nav navbar-nav navbar-right">\n\n')
        if request.user.username != '':
            __M_writer('\n                <li><a href="/homepage/index.logout_view/">Logout</a></li>\n                <li><a>')
            __M_writer(str(request.user.username))
            __M_writer('</a></li>\n\n')
        else:
            __M_writer('\n                <li><a href="#" id="show_login_modal">Login</a></li>\n\n')
        __M_writer('\n\n\n              </ul>\n            </div><!-- /.navbar-collapse -->\n          </div><!-- /.container-fluid -->\n        </nav>\n\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admin(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admin():
            return render_admin(context)
        def header():
            return render_header(context)
        def center():
            return render_center(context)
        request = context.get('request', UNDEFINED)
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer(' <!-- header -->\n\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer(' <!-- center -->\n\n\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer(' <!-- footer -->\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="footer">\n      <nav class="footer navbar navbar-fixed-bottom">\n      </nav>\n    </div>\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/base.htm", "source_encoding": "ascii", "uri": "base.htm", "line_map": {"66": 103, "131": 80, "72": 103, "141": 96, "78": 11, "147": 89, "85": 11, "86": 33, "87": 34, "88": 49, "89": 61, "90": 62, "91": 64, "92": 64, "93": 66, "94": 67, "95": 71, "165": 4, "27": 0, "101": 83, "171": 165, "107": 83, "45": 1, "113": 8, "50": 6, "55": 101, "153": 89, "136": 85, "159": 4, "60": 105, "126": 8}}
__M_END_METADATA
"""
