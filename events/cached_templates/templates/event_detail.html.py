# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428173808.334596
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/events/templates/event_detail.html'
_template_uri = 'event_detail.html'
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
        event = context.get('event', UNDEFINED)
        products = context.get('products', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        event = context.get('event', UNDEFINED)
        products = context.get('products', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container">\n\n            <!-- Jumbotron Header -->\n            <header class="jumbotron hero-spacer">\n                <h1>')
        __M_writer(str( event.name ))
        __M_writer('</h1>\n                <p> ')
        __M_writer(str( event.description ))
        __M_writer('</p>\n                <p><a class="btn btn-primary btn-large">\'Merica\'!</a>\n                </p>\n            </header>\n\n            <hr>\n\n            <!-- Title -->\n            <div class="row">\n                <div class="col-lg-12">\n                    <h3>Featured Areas</h3>\n                </div>\n            </div>\n            <!-- /.row -->\n\n            <!-- Page Features -->\n            <div class="row text-center items">\n\n')
        for area in areas:
            __M_writer('\n                <div class="col-md-3 col-sm-6 hero-feature">\n                    <div class="thumbnail">\n                        <img class="item_image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('events/media/area_images/')
            __M_writer(str( area.id))
            __M_writer('.jpg" alt="">\n                        <div class="caption">\n                            <h3>')
            __M_writer(str( area.name ))
            __M_writer('</h3>\n                            <p>')
            __M_writer(str( area.description ))
            __M_writer('</p>\n                        </div>\n                    </div>\n                </div>\n\n')
        __M_writer('\n\n            </div>\n            <!-- /.row -->\n\n            <!-- Title -->\n            <div class="row">\n                <div class="col-lg-12">\n                    <h3>Products For Sale</h3>\n                </div>\n            </div>\n            <!-- /.row -->\n\n            <!-- Page Features -->\n            <div class="row text-center items">\n\n')
        for product in products:
            __M_writer('\n                <div class="col-md-3 col-sm-6 hero-feature">\n                    <div class="thumbnail">\n                        <img class="item_image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('shop/media/product_images/')
            __M_writer(str( product.id))
            __M_writer('.jpg" alt="">\n                        <div class="caption">\n                            <h3>')
            __M_writer(str( product.name ))
            __M_writer('</h3>\n                            <p>')
            __M_writer(str( product.description ))
            __M_writer('</p>\n                        </div>\n                    </div>\n                </div>\n\n')
        __M_writer('\n\n            </div>\n            <!-- /.row -->\n\n            <hr>\n\n            <!-- Footer -->\n            <footer>\n                <div class="row">\n                    <div class="col-lg-12">\n                        <p>Copyright Your Website 2014</p>\n                    </div>\n                </div>\n            </footer>\n\n        </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "event_detail.html", "line_map": {"64": 27, "65": 28, "66": 31, "67": 31, "68": 31, "69": 31, "70": 33, "71": 33, "72": 34, "73": 34, "74": 40, "75": 56, "76": 57, "77": 60, "78": 60, "79": 60, "80": 60, "81": 62, "82": 62, "83": 63, "84": 63, "85": 69, "27": 0, "91": 85, "38": 1, "43": 87, "49": 3, "59": 3, "60": 8, "61": 8, "62": 9, "63": 9}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/events/templates/event_detail.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
