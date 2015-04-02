# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427834879.062335
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/index.html'
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        login_required = context.get('login_required', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        login_required = context.get('login_required', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if login_required:
            __M_writer('  <div id="login_alert" class="alert alert-success alert-dismissible col-sm-2" role="alert">\n    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n    Please login to checkout\n  </div>\n\n')
        __M_writer('\n\n\n<div class="container">\n\n        <!-- Jumbotron Header -->\n        <header class="jumbotron hero-spacer">\n            <h1>Online Store</h1>\n            <p>Come see our assortment of Colonial American swag.  Other historical items are of especially good value.</p>\n            <p><a class="btn btn-primary btn-large">\'Merica\'!</a>\n            </p>\n        </header>\n\n        <hr>\n\n        <!-- Title -->\n        <div class="row">\n            <div class="col-lg-12">\n                <h3>Latest Features</h3>\n            </div>\n        </div>\n        <!-- /.row -->\n\n        <!-- Page Features -->\n        <div class="row text-center items">\n\n')
        for item in items:
            __M_writer('\n            <div class="col-md-3 col-sm-6 hero-feature">\n                <div class="thumbnail">\n                    <img class="item_image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('shop/media/product_images/')
            __M_writer(str( item.id))
            __M_writer('.jpg" alt="">\n                    <div class="caption">\n                        <h3>')
            __M_writer(str( item.name ))
            __M_writer('</h3>\n                        <p>')
            __M_writer(str( item.description ))
            __M_writer('</p>\n                        <p>\n                            <a href="#" data-id="')
            __M_writer(str( item.id))
            __M_writer('" data-product="True" class="btn btn-primary add_to_cart">Add to Cart</a> <a href="/shop/item_detail/')
            __M_writer(str( item.id ))
            __M_writer('" class="btn btn-default">More Info</a>\n                        </p>\n                    </div>\n                </div>\n            </div>\n\n')
        __M_writer('\n\n        </div>\n        <!-- /.row -->\n\n        <hr>\n\n        <!-- Footer -->\n        <footer>\n            <div class="row">\n                <div class="col-lg-12">\n                    <p>Copyright Your Website 2014</p>\n                </div>\n            </div>\n        </footer>\n\n    </div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/index.html", "uri": "index.html", "line_map": {"64": 42, "65": 42, "66": 42, "67": 44, "68": 44, "69": 45, "70": 45, "71": 47, "72": 47, "73": 47, "74": 47, "75": 54, "81": 75, "27": 0, "37": 1, "42": 75, "48": 3, "57": 3, "58": 5, "59": 6, "60": 12, "61": 38, "62": 39, "63": 42}}
__M_END_METADATA
"""
