# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428211912.125172
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'meta', 'shop', 'footer', 'foot_links', 'head_links', 'header']


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
        def meta():
            return render_meta(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        num_items = context.get('num_items', UNDEFINED)
        def head_links():
            return render_head_links(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\n\n\n<!-- CSS/JS Links that belong only to the shop app -->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer(' <!-- head_links -->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shop'):
            context['self'].shop(**pageargs)
        

        __M_writer(' <!-- shop -->\n\n')
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
        __M_writer('\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\n<meta charset="UTF-8">\n<meta name="description" content="Colonial American Products for sale">\n<meta name="keywords" content="Colonial America Products Sale">\n<meta name="author" content="Dan Morain">\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        def shop():
            return render_shop(context)
        def footer():
            return render_footer(context)
        num_items = context.get('num_items', UNDEFINED)
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer(' <!-- center -->\n\n\n\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer(' <!-- footer -->\n\n')
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


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n<link href="http://ironsummitmedia.github.io/startbootstrap-heroic-features/css/bootstrap.min.css" rel="stylesheet">\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        num_items = context.get('num_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <!-- Navbar -->\n  <nav class="navbar navbar-default navbar-fixed-top">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="/homepage/index/">Colonial Heritage Foundation</a>\n          </div>\n\n          <!-- Collect the nav links, forms, and other content for toggling -->\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n\n            <ul class="nav navbar-nav">\n              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Shop<span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="/shop/index/">Sale Items</a></li>\n                  <li><a href="/shop/index.rentals/">Rental Item</a></li>\n                </ul>\n              </li>\n              <li id="tab"><a href="/events/index/">Events</a></li>\n\n            </ul>\n\n            <form class="navbar-form navbar-left" id="search_form" method="POST" action="/shop/index.search/" role="search">\n              <div class="form-group">\n\n                  <input type="text" id="search_input" class="form-control" placeholder="Search">\n\n              </div>\n              <button id="search" type="submit" class="btn btn-success">Go</button>\n            </form>\n            <ul class="nav navbar-nav navbar-right">\n              <li><a href="#" id="show_cart" >Cart <span class="badge"> ')
        __M_writer(str( num_items))
        __M_writer(' </span></a></li>\n\n\n\n')
        if request.user.username != '':
            __M_writer('\n              <li><a href="/shop/index.logout_view/">Logout</a></li>\n              <li class="dropdown">\n                <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">')
            __M_writer(str(request.user.username))
            __M_writer(' <span class="caret"></span></a>\n                <ul class="dropdown-menu" role="menu">\n                  <li><a href="/shop/myaccount/">My Account</a></li>\n                </ul>\n              </li>\n\n')
        else:
            __M_writer('\n              <li><a href="#" id="show_login_modal">Login</a></li>\n              <li><a href="#" id="show_signup_modal">Signup</a></li>\n\n')
        __M_writer('\n\n\n            </ul>\n          </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n      </nav> <!-- navbar -->\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/base.htm", "source_encoding": "ascii", "uri": "base.htm", "line_map": {"192": 186, "181": 68, "68": 114, "133": 101, "74": 94, "139": 101, "80": 94, "145": 112, "122": 96, "86": 4, "151": 112, "186": 83, "27": 0, "92": 4, "157": 14, "48": 1, "98": 21, "163": 14, "169": 23, "112": 21, "177": 23, "178": 63, "179": 63, "180": 67, "117": 91, "182": 71, "183": 71, "184": 77, "185": 78, "58": 19, "63": 110, "53": 10, "127": 108}}
__M_END_METADATA
"""
