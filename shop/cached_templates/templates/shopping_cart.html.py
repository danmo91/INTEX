# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427924891.100137
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="items">\n      <table class="table table-striped">\n        <thead>\n          <tr>\n            <th>Name</th>\n            <th>Quantity</th>\n            <th>Price</th>\n            <th>Total</th>\n            <th>Action</th>\n          </tr>\n        </thead>\n\n        <tbody>\n\n        ')

        total = 0
        rental_total = 0
                
        
        __M_writer('\n\n')
        for key,value in items.items():
            __M_writer('        ')

            price = value[0].current_price
            qty = value[1]
            
            sub_total =  price * qty
            total += sub_total
                    
            
            __M_writer('\n          <tr>\n            <td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( value[1] ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( value[0].current_price ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( sub_total ))
            __M_writer("</td>\n            <td><a data-id='")
            __M_writer(str( value[0].id))
            __M_writer('\' data-product=\'True\' class="btn btn-primary delete_from_cart">Remove</a></td>\n          </tr>\n')
        __M_writer('\n        </tbody>\n\n        <tfoot>\n          <tr>\n            <td> </td>\n            <td> </td>\n            <td> </td>\n            <td id="total_row">$')
        __M_writer(str( total ))
        __M_writer('</td>\n          </tr>\n        </tfoot>\n\n      </table>\n\n  </div>\n\n  <div class="rentals">\n      <table class="table table-striped">\n        <thead>\n          <tr>\n            <th>Name</th>\n            <th>Rental Price</th>\n            <th>Action</th>\n          </tr>\n        </thead>\n\n        <tbody>\n\n')
        for rental in rentals:
            __M_writer('        ')
            rental_total += rental.value 
            
            __M_writer('\n          <tr>\n            <td>')
            __M_writer(str( rental.name ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( rental.value ))
            __M_writer("</td>\n            <td><a data-id='")
            __M_writer(str( rental.id))
            __M_writer('\' data-product=\'False\' class="btn btn-primary delete_from_cart">Remove</a></td>\n          </tr>\n')
        __M_writer('\n        </tbody>\n\n        <tfoot>\n          <tr>\n            <td> </td>\n            <td> </td>\n            <td> </td>\n            <td id="total_row">$')
        __M_writer(str( rental_total ))
        __M_writer('</td>\n          </tr>\n        </tfoot>\n\n      </table>\n\n  </div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 27, "72": 33, "73": 35, "74": 35, "75": 36, "76": 36, "77": 37, "78": 37, "79": 38, "80": 38, "81": 39, "82": 39, "83": 42, "84": 50, "85": 50, "86": 70, "87": 71, "88": 71, "90": 71, "27": 0, "92": 73, "93": 74, "94": 74, "95": 75, "96": 75, "97": 78, "98": 86, "91": 73, "36": 1, "41": 96, "47": 5, "99": 86, "105": 99, "55": 5, "56": 21, "61": 24, "62": 26, "63": 27}, "source_encoding": "ascii", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/shopping_cart.html", "uri": "shopping_cart.html"}
__M_END_METADATA
"""
