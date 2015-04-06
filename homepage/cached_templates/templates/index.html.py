# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428360417.843102
_enable_loop = True
_template_filename = 'C:\\Users\\brian_000\\projects\\intex\\homepage\\templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="center">\r\n    <div class="container homepagey">\r\n      <div class="jumbotron">\r\n\r\n        <h1 class="chffont">Colonial Heritage Foundation</h1>\r\n\r\n      </div>\r\n\r\n      <div class="row breaker">\r\n        <h2 class="dropshadow">Welcomes You</h2>\r\n        <p>Feel free to stay a while.... Shop around. Rent items. Explore Events.</p>\r\n      </div>\r\n\r\n      <div class="row">\r\n        <div class="col-sm-4">\r\n          <h3>Divine Providence</h3>\r\n          <img src="/static/homepage/media/images/divinep.jpg" style="height:200px;width:280px;border-radius:5px">\r\n        </div>\r\n        <div class="col-sm-4">\r\n          <h3>Equal Rights</h3>\r\n        <img src="/static/homepage/media/images/const.jpg" style="height:200px;width:280px;border-radius:5px">\r\n        </div>\r\n        <div class="col-sm-4">\r\n          <h3>Liberty For All</h3>\r\n        <img src="/static/homepage/media/images/liberty.jpg" style="height:200px;width:280px;border-radius:5px">\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <hr>\r\n\r\n  <!-- Footer -->\r\n  <footer>\r\n      <div class="row">\r\n          <div class="col-lg-12">\r\n              <div class="navbar-text pull-right">\r\n                  <h4>Follow us on:</h4>\r\n                  <a href="https://www.facebook.com/dan.morain.5"><i class="fa fa-facebook-square fa-3x"></i></a>\r\n                  <a href="https://twitter.com/DanMorain91"><i class="fa fa-twitter fa-3x"></i></a>\r\n                  <a href="https://plus.google.com/+DanMorain/posts/p/pub"><i class="fa fa-google-plus fa-3x"></i></a>\r\n                  <a href="https://instagram.com/danmo91/"><i class="fa fa-instagram fa-3x"></i></a>\r\n              </div>\r\n          </div>\r\n      </div>\r\n  </footer>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"34": 1, "51": 3, "39": 52, "57": 51, "27": 0, "45": 3}, "source_encoding": "ascii", "filename": "C:\\Users\\brian_000\\projects\\intex\\homepage\\templates/index.html"}
__M_END_METADATA
"""
