# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428024608.967333
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/confirm_order.html'
_template_uri = 'confirm_order.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'center']



import datetime


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
        def header():
            return render_header(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        round = context.get('round', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        rentals = context.get('rentals', UNDEFINED)
        round = context.get('round', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container">\n\t<div class="row form-group">\n        <div class="col-xs-12">\n            <ul class="nav nav-pills nav-justified thumbnail setup-panel">\n                <li class="active"><a href="#step-1"\n                    <h4 class="list-group-item-heading">Step 1</h4>\n                    <p class="list-group-item-text">Confirm Order</p>\n                </a></li>\n                <li class="disabled"><a href="#step-2">\n                    <h4 class="list-group-item-heading">Step 2</h4>\n                    <p class="list-group-item-text">Enter Payment</p>\n                </a></li>\n                <li class="disabled"><a href="#step-3">\n                    <h4 class="list-group-item-heading">Step 3</h4>\n                    <p class="list-group-item-text">Thank You</p>\n                </a></li>\n            </ul>\n        </div>\n\t</div>\n\n</div>\n\n<div class="container">\n\t<div class="row">\n\t\t<div class="col-xs-12">\n\t\t\t<div class="panel panel-info">\n\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t<div class="panel-title">\n\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t<div class="col-xs-6">\n\t\t\t\t\t\t\t\t<h5><span class="glyphicon glyphicon-shopping-cart"></span> Shopping Cart</h5>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="panel-body">\n\n          ')

        total = 0
        sub_total = 0
                   
        
        __M_writer('\n\n\t\t\t\t\t<div class="items">\n')
        for key,value in items.items():
            __M_writer('\n\t          ')

            price = value[0].current_price
            qty = value[1]
            
            sub_total =  price * qty
            total += sub_total
                              
            
            __M_writer('\n\n\t          <!-- row -->\n\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t<div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="col-xs-4">\n\t\t\t\t\t\t\t\t<h4 class="product-name"><strong>')
            __M_writer(str( value[0].name ))
            __M_writer('</strong></h4><h4><small>')
            __M_writer(str( value[0].description))
            __M_writer('</small></h4>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="col-xs-6">\n\t\t\t\t\t\t\t\t<div class="col-xs-6 text-right">\n\t\t\t\t\t\t\t\t\t<h6><strong>')
            __M_writer(str( value[0].current_price ))
            __M_writer('<span class="text-muted"></span></strong></h6>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="col-xs-4">\n\t                <h6><strong>')
            __M_writer(str( value[1] ))
            __M_writer('<span class="text-muted"></span></span></strong></h6>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<hr>\n\t          <!-- end row -->\n\n')
        __M_writer('\t\t\t\t\t</div>\n\n\t\t\t\t\t<h4>Rental Items</h4>\n\t\t\t\t\t<hr>\n\n\t\t\t\t\t<div class="rentals">\n')
        for rental in rentals:
            __M_writer('\n\t          ')

            total += rental.rental_price
                              
            
            __M_writer('\n\n\t          <!-- row -->\n\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t<div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="col-xs-4">\n\t\t\t\t\t\t\t\t<h4 class="product-name"><strong>')
            __M_writer(str( rental.name ))
            __M_writer('</strong></h4><h4><small>')
            __M_writer(str( rental.description))
            __M_writer('</small></h4>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="col-xs-6">\n\t\t\t\t\t\t\t\t<div class="col-xs-6 text-right">\n\t\t\t\t\t\t\t\t\t<h6><strong>')
            __M_writer(str( rental.rental_price ))
            __M_writer('<span class="text-muted"></span></strong></h6>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="col-xs-4">\n\t                <h6><strong>Due Date: <span class="text-muted">')
            __M_writer(str( datetime.date.today() + datetime.timedelta(days=30) ))
            __M_writer('</span></span></strong></h6>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<hr>\n\t          <!-- end row -->\n\n')
        __M_writer('\t\t\t\t\t</div>\n\n\n\n\n\t\t\t\t</div>\n\t\t\t\t<div class="panel-footer">\n\t\t\t\t\t<div class="row text-center">\n\t\t\t\t\t\t<div class="col-xs-9">\n\t\t\t\t\t\t\t<h4 class="text-right">Total <strong>')
        __M_writer(str( round(total,2) ))
        __M_writer('</strong></h4>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="col-xs-3">\n\t\t\t\t\t\t\t<a href="/shop/checkout.enter_payment/" class="btn btn-success btn-block">\n\t\t\t\t\t\t\t\tContinue\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "confirm_order.html", "source_encoding": "ascii", "line_map": {"66": 7, "107": 86, "118": 103, "72": 11, "108": 92, "16": 3, "81": 11, "82": 50, "131": 125, "124": 127, "87": 53, "88": 56, "89": 57, "90": 58, "31": 0, "98": 64, "99": 71, "100": 71, "101": 71, "102": 71, "103": 75, "104": 75, "105": 78, "106": 78, "43": 1, "44": 5, "109": 93, "110": 94, "49": 9, "114": 96, "115": 103, "116": 103, "117": 103, "54": 143, "119": 107, "120": 107, "121": 110, "122": 110, "123": 118, "60": 7, "125": 127}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/confirm_order.html"}
__M_END_METADATA
"""
