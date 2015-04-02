# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427439083.59751
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/products.html'
_template_uri = 'products.html'
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
        products = context.get('products', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Products</h1>\n      </div>\n    </div>\n\n\n    <a href="/manager/products.create/" id="btn_create" class="btn btn-success pull-right create">Create new product</a>\n\n\t\t<table class="table table-striped table-bordered table-hover">\n\n      <thead>\n\n        <tr>\n  \t\t\t\t<th>Name</th>\n  \t\t\t\t<th>Description</th>\n  \t\t\t\t<th>Category</th>\n  \t\t\t\t<th>Price</th>\n  \t\t\t\t<th>Actions</th>\n  \t\t\t</tr>\n\n      </thead>\n\n      <tbody>\n\n')
        for product in products:
            __M_writer('  \t\t\t\t<tr>\n  \t\t\t\t\t<td>')
            __M_writer(str( product.name ))
            __M_writer('</td>\n  \t\t\t\t\t<td>')
            __M_writer(str( product.description ))
            __M_writer('</td>\n  \t\t\t\t\t<td>')
            __M_writer(str( product.category ))
            __M_writer('</td>\n  \t\t\t\t\t<td>$')
            __M_writer(str( product.current_price ))
            __M_writer('</td>\n  \t\t\t\t\t<td>\n  \t\t\t\t\t\t<a href="/manager/products.edit/')
            __M_writer(str(product.id))
            __M_writer('"/> Edit </a>\n  \t\t\t\t\t\t|\n  \t\t\t\t\t\t<a href="/manager/products.delete/')
            __M_writer(str(product.id))
            __M_writer('"> Delete </a>\n\n\n  \t\t\t\t\t</td>\n  \t\t\t\t</tr>\n')
        __M_writer('\n      </tbody>\n\n\t\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 37, "65": 37, "66": 39, "35": 1, "68": 45, "40": 50, "74": 68, "46": 3, "59": 33, "67": 39, "53": 3, "54": 30, "55": 31, "56": 32, "57": 32, "58": 33, "27": 0, "60": 34, "61": 34, "62": 35, "63": 35}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/products.html", "uri": "products.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
