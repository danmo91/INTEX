# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427932966.753539
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/receipt.html'
_template_uri = 'receipt.html'
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
        int = context.get('int', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
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
        int = context.get('int', UNDEFINED)
        def center():
            return render_center(context)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <h1>Receipt</h1>\n\n  <h3>\n    Thank you for shopping with us!\n  </h3>\n\n\n\n  <p>\n    Order Summary:\n  </p>\n  <div class="items">\n\n    <table class="table table-striped">\n      <thead>\n        <tr>\n          <th>Name</th>\n          <th>Quantity</th>\n          <th>Price</th>\n          <th>Total</th>\n        </tr>\n      </thead>\n\n\n    ')
        total = 0 
        
        __M_writer('\n\n    <tbody>\n\n')
        for key,value in items.items():
            __M_writer('\n    ')

            price = int(value[0].value)
            qty = value[1]
            
            sub_total =  price * qty
            total += sub_total
                
            
            __M_writer('\n\n\n\n        <tr>\n          <td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n          <td>\n\n            ')
            __M_writer(str( value[1] ))
            __M_writer('\n\n          </td>\n          <td>$')
            __M_writer(str( value[0].value ))
            __M_writer('</td>\n          <td>$')
            __M_writer(str( sub_total ))
            __M_writer('</td>\n        </tr>\n\n\n\n')
        __M_writer('    </tbody>\n\n\n      <tfoot>\n        <tr>\n          <td> </td>\n          <td> </td>\n          <td> </td>\n          <td id="total_row">$')
        __M_writer(str( total ))
        __M_writer('</td>\n        </tr>\n      </tfoot>\n\n\n    </table>\n\n  </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"69": 41, "70": 46, "71": 46, "72": 49, "73": 49, "74": 52, "75": 52, "76": 53, "77": 53, "78": 59, "79": 67, "80": 67, "86": 80, "27": 0, "36": 1, "41": 77, "47": 3, "55": 3, "56": 29, "58": 29, "59": 33, "60": 34, "61": 35}, "source_encoding": "ascii", "uri": "receipt.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/receipt.html"}
__M_END_METADATA
"""
