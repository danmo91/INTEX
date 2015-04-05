# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428175265.927537
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/homepage/templates/index.html'
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
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="center">\n    <div class="container">\n      <div class="jumbotron">\n\n        <h1>Ask. Explore. Discover.</h1>\n        <p>What are you capable of?</p>\n\n      </div>\n\n      <div class="row">\n        <div class="col-sm-4">\n          <h3>Focus</h3>\n          <img src="/static/homepage/media/images/yosemite.jpg" style="height:200px;width:250px;border-radius:5px">\n        <p style="width:250px">If we try to do everything, how can we perfect anything?</p>\n        </div>\n        <div class="col-sm-4">\n          <h3>Simplify</h3>\n        <img src="http://media.treehugger.com/assets/images/2011/10/fashion-sustainable-fair-trade.jpg" style="height:200px;width:250px;border-radius:5px">\n          <p style="width:250px">Remove anything that distracts from your purpose</p>\n        </div>\n        <div class="col-sm-4">\n          <h3>Perfect</h3>\n        <img src="http://upload.wikimedia.org/wikipedia/commons/b/b2/Tea_bowl_fixed_in_the_Kintsugi_method.jpg" style="height:200px;width:250px;border-radius:5px">\n          <p style="width:250px">Start again...and again...and again</p>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <hr>\n\n  <!-- Footer -->\n  <footer>\n      <div class="row">\n          <div class="col-lg-12">\n              <div class="navbar-text pull-right">\n                  <h4>Follow us on:</h4>\n                  <a href="https://www.facebook.com/dan.morain.5"><i class="fa fa-facebook-square fa-3x"></i></a>\n                  <a href="https://twitter.com/DanMorain91"><i class="fa fa-twitter fa-3x"></i></a>\n                  <a href="https://plus.google.com/+DanMorain/posts/p/pub"><i class="fa fa-google-plus fa-3x"></i></a>\n                  <a href="https://instagram.com/danmo91/"><i class="fa fa-instagram fa-3x"></i></a>\n              </div>\n          </div>\n      </div>\n  </footer>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"34": 1, "51": 3, "39": 51, "57": 51, "27": 0, "45": 3}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/homepage/templates/index.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
