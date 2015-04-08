# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428453511.408071
_enable_loop = True
_template_filename = 'C:\\Users\\brian_000\\projects\\intex\\shop\\templates/index.html'
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
        login_required = context.get('login_required', UNDEFINED)
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        login_required = context.get('login_required', UNDEFINED)
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if login_required:
            __M_writer('  <div id="login_alert" class="alert alert-success alert-dismissible col-sm-2" role="alert">\r\n    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n    Please login to checkout\r\n  </div>\r\n\r\n')
        __M_writer('\r\n\r\n\r\n<div class="container shopstyle">\r\n\r\n        <!-- Jumbotron Header -->\r\n        <header class="jumbotron hero-spacer">\r\n            <h1>Online Store</h1>\r\n        </header>\r\n\r\n        <hr>\r\n\r\n        <div class="row breaker">\r\n          <p>Come see our assortment of Colonial American swag.  Other historical items are of especially good value.</p>\r\n          </p>\r\n        </div>\r\n\r\n        <!-- Title -->\r\n        <div class="row">\r\n            <div class="col-lg-12">\r\n                <h3>Latest Features</h3>\r\n            </div>\r\n        </div>\r\n        <!-- /.row -->\r\n\r\n        <!-- Page Features -->\r\n        <div class="row text-center items">\r\n\r\n')
        for item in items:
            __M_writer('\r\n            <div class="col-md-3 col-sm-6 hero-feature">\r\n                <div class="thumbnail">\r\n                    <img class="item_image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('shop/media/product_images/')
            __M_writer(str( item.id))
            __M_writer('.jpg" alt="">\r\n                    <div class="caption">\r\n                        <h3>')
            __M_writer(str( item.name ))
            __M_writer('</h3>\r\n                        <p>')
            __M_writer(str( item.description ))
            __M_writer('</p>\r\n                          <p>\r\n                            <a href="#" data-id="')
            __M_writer(str( item.id))
            __M_writer('" data-product="True" class="btn btn-primary add_to_cart">Add to Cart</a> <a href="/shop/item_detail/')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-default">More Info</a>\r\n                        </p>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n\r\n')
        __M_writer('\r\n\r\n        </div>\r\n        <!-- /.row -->\r\n\r\n        <hr>\r\n\r\n        <!-- Footer -->\r\n        <footer>\r\n            <div class="row">\r\n                <div class="col-lg-12">\r\n                    <p>Copyright Your Website 2014</p>\r\n                </div>\r\n            </div>\r\n        </footer>\r\n\r\n    </div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\brian_000\\projects\\intex\\shop\\templates/index.html", "line_map": {"64": 44, "65": 44, "66": 44, "67": 46, "68": 46, "69": 47, "70": 47, "71": 49, "72": 49, "73": 49, "74": 49, "75": 56, "81": 75, "27": 0, "37": 1, "42": 77, "48": 3, "57": 3, "58": 5, "59": 6, "60": 12, "61": 40, "62": 41, "63": 44}, "source_encoding": "ascii", "uri": "index.html"}
__M_END_METADATA
"""
