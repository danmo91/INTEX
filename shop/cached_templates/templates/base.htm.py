# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428174075.95165
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['head_links', 'footer', 'foot_links', 'shop', 'header', 'center']


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
        def head_links():
            return render_head_links(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        num_items = context.get('num_items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
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


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        num_items = context.get('num_items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def shop():
            return render_shop(context)
        def header():
            return render_header(context)
        def center():
            return render_center(context)
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


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        num_items = context.get('num_items', UNDEFINED)
        request = context.get('request', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"67": 5, "132": 99, "161": 85, "73": 5, "138": 14, "79": 92, "146": 14, "147": 54, "148": 54, "149": 58, "150": 59, "151": 62, "152": 62, "153": 68, "154": 69, "27": 0, "97": 103, "91": 103, "103": 12, "167": 85, "173": 167, "46": 1, "51": 10, "155": 74, "117": 12, "56": 101, "122": 82, "61": 105, "85": 92, "127": 87}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
