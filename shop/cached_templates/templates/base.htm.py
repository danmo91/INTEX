# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428360480.914219
_enable_loop = True
_template_filename = 'C:\\Users\\brian_000\\projects\\intex\\shop\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'meta', 'header', 'footer', 'foot_links', 'shop', 'head_links']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        num_items = context.get('num_items', UNDEFINED)
        def shop():
            return render_shop(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def meta():
            return render_meta(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def head_links():
            return render_head_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\r\n\r\n\r\n<!-- CSS/JS Links that belong only to the shop app -->\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer(' <!-- head_links -->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shop'):
            context['self'].shop(**pageargs)
        

        __M_writer(' <!-- shop -->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer(' <!-- foot_links -->\r\n')
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
        __M_writer('\r\n<meta charset="UTF-8">\r\n<meta name="description" content="Colonial American Products for sale">\r\n<meta name="keywords" content="Colonial America Products Sale">\r\n<meta name="author" content="Dan Morain">\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        num_items = context.get('num_items', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  <!-- Navbar -->\r\n  <nav class="navbar navbar-default navbar-fixed-top">\r\n        <div class="container-fluid">\r\n          <!-- Brand and toggle get grouped for better mobile display -->\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n              <span class="sr-only">Toggle navigation</span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="/homepage/index/">Colonial Heritage Foundation</a>\r\n          </div>\r\n\r\n          <!-- Collect the nav links, forms, and other content for toggling -->\r\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n\r\n            <ul class="nav navbar-nav">\r\n              <li class="dropdown">\r\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Shop<span class="caret"></span></a>\r\n                <ul class="dropdown-menu" role="menu">\r\n                  <li><a href="/shop/index/">Sale Items</a></li>\r\n                  <li><a href="/shop/index.rentals/">Rental Item</a></li>\r\n                </ul>\r\n              </li>\r\n              <li id="tab"><a href="/events/index/">Events</a></li>\r\n\r\n            </ul>\r\n\r\n            <form class="navbar-form navbar-left" id="search_form" method="POST" action="/shop/index.search/" role="search">\r\n              <div class="form-group">\r\n\r\n                  <input type="text" id="search_input" class="form-control" placeholder="Search">\r\n\r\n              </div>\r\n              <button id="search" type="submit" class="btn btn-success">Go</button>\r\n            </form>\r\n            <ul class="nav navbar-nav navbar-right">\r\n              <li><a href="#" id="show_cart" >Cart <span class="badge"> ')
        __M_writer(str( num_items))
        __M_writer(' </span></a></li>\r\n\r\n\r\n\r\n')
        if request.user.username != '':
            __M_writer('\r\n              <li><a href="/shop/index.logout_view/">Logout</a></li>\r\n              <li class="dropdown">\r\n                <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">')
            __M_writer(str(request.user.first_name))
            __M_writer(' <span class="caret"></span></a>\r\n                <ul class="dropdown-menu" role="menu">\r\n                  <li><a href="/shop/myaccount/">My Account</a></li>\r\n                </ul>\r\n              </li>\r\n\r\n')
        else:
            __M_writer('\r\n              <li><a href="#" id="show_login_modal">Login</a></li>\r\n              <li><a href="#" id="show_signup_modal">Signup</a></li>\r\n\r\n')
        __M_writer('\r\n\r\n\r\n            </ul>\r\n          </div><!-- /.navbar-collapse -->\r\n        </div><!-- /.container-fluid -->\r\n      </nav> <!-- navbar -->\r\n\r\n  ')
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


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        num_items = context.get('num_items', UNDEFINED)
        def center():
            return render_center(context)
        def header():
            return render_header(context)
        def shop():
            return render_shop(context)
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer(' <!-- center -->\r\n\r\n\r\n\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer(' <!-- footer -->\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<link href="http://ironsummitmedia.github.io/startbootstrap-heroic-features/css/bootstrap.min.css" rel="stylesheet">\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"192": 186, "68": 114, "133": 112, "74": 94, "139": 112, "80": 94, "145": 21, "174": 108, "86": 4, "27": 0, "92": 4, "186": 14, "159": 21, "48": 1, "98": 23, "164": 91, "169": 96, "106": 23, "107": 63, "108": 63, "109": 67, "110": 68, "111": 71, "112": 71, "113": 77, "114": 78, "115": 83, "180": 14, "53": 10, "121": 101, "58": 19, "127": 101, "63": 110}, "source_encoding": "ascii", "filename": "C:\\Users\\brian_000\\projects\\intex\\shop\\templates/base.htm"}
__M_END_METADATA
"""
