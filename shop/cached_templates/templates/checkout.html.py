# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427926139.85769
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/checkout.html'
_template_uri = 'checkout.html'
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
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="jumbotron">\n  <div class="container">\n    <h1>Checkout</h1>\n  </div>\n</div>\n\n\n  <div class="items">\n\n    <table class="table table-striped">\n      <thead>\n        <tr>\n          <th>Name</th>\n          <th>Quantity</th>\n          <th>Price</th>\n          <th>Total</th>\n        </tr>\n      </thead>\n\n\n    ')
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
        __M_writer('</td>\n        </tr>\n      </tfoot>\n\n\n    </table>\n\n  </div>\n\n\n\n  <div class="panel panel-default">\n    <div class="panel-heading">\n      <h3 class="panel-title">Shipping and Credit Card</h3>\n    </div>\n    <div class="panel-body">\n\n      <!-- <form id="checkoutform" method="POST" action="/shop/receipt/">\n\n        <table>\n\n          ')
        __M_writer(str(form))
        __M_writer('\n\n        </table>\n\n        <input value="Checkout" type="submit" class="btn btn-success"/>\n      </form> -->\n\n\n      <form class=form-signin id="checkoutform" method="POST" action="/shop/receipt/">\n\n')
        for field in form:
            __M_writer('\n          <label class="sr-only"> ')
            __M_writer(str( field.name ))
            __M_writer('</label>\n\n          ')
            print('Field:',field) 
            
            __M_writer('\n\n            ')
            __M_writer(str( field ))
            __M_writer('\n\n')
        __M_writer('\n        <button class="btn btn-lg btn-primary btn-block" type="submit">Checkout</button>\n\n      </form>\n\n    </div>\n    <div class="panel-footer">\n\n    </div>\n  </div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/checkout.html", "line_map": {"71": 37, "72": 42, "73": 42, "74": 45, "75": 45, "76": 48, "77": 48, "78": 49, "79": 49, "80": 55, "81": 63, "82": 63, "83": 84, "84": 84, "85": 94, "86": 95, "87": 96, "88": 96, "89": 98, "27": 0, "92": 100, "93": 100, "94": 103, "91": 98, "100": 94, "37": 1, "42": 117, "48": 3, "57": 3, "58": 25, "60": 25, "61": 29, "62": 30, "63": 31}, "source_encoding": "ascii", "uri": "checkout.html"}
__M_END_METADATA
"""
