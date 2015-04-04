# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428099706.011756
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/email_receipt.html'
_template_uri = 'email_receipt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'header']


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
        rentals = context.get('rentals', UNDEFINED)
        address = context.get('address', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        round = context.get('round', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
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


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentals = context.get('rentals', UNDEFINED)
        address = context.get('address', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def center():
            return render_center(context)
        request = context.get('request', UNDEFINED)
        round = context.get('round', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container">\n\t<div class="row">\n\t\t<div class="col-xs-12">\n\t\t\t<div class="panel panel-info">\n\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t<div class="panel-title">\n\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t<div class="col-xs-6">\n\t\t\t\t\t\t\t\t<h5><span class="glyphicon glyphicon-thumbs-up"></span> Order Summary</h5>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="panel-body">\n\n          ')

        total = 0
        sub_total = 0
        
                   
        
        __M_writer('\n\n          <div class="items">\n')
        for key,value in items.items():
            __M_writer('\n            ')

            price = value[0].current_price
            qty = value[1]
            
            sub_total =  price * qty
            total += sub_total
                        
            
            __M_writer('\n\n            <!-- row -->\n  \t\t\t\t\t<div class="row">\n  \t\t\t\t\t\t<div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\n  \t\t\t\t\t\t</div>\n  \t\t\t\t\t\t<div class="col-xs-4">\n  \t\t\t\t\t\t\t<h4 class="product-name"><strong>')
            __M_writer(str( value[0].name ))
            __M_writer('</strong></h4><h4><small>')
            __M_writer(str( value[0].description))
            __M_writer('</small></h4>\n  \t\t\t\t\t\t</div>\n  \t\t\t\t\t\t<div class="col-xs-6">\n  \t\t\t\t\t\t\t<div class="col-xs-6 text-right">\n  \t\t\t\t\t\t\t\t<h6><strong>')
            __M_writer(str( value[0].current_price ))
            __M_writer('<span class="text-muted">x</span></strong></h6>\n  \t\t\t\t\t\t\t</div>\n  \t\t\t\t\t\t\t<div class="col-xs-4">\n                  <h6><strong>')
            __M_writer(str( value[1] ))
            __M_writer('<span class="text-muted"></span></span></strong></h6>\n  \t\t\t\t\t\t\t</div>\n  \t\t\t\t\t\t</div>\n  \t\t\t\t\t</div>\n  \t\t\t\t\t<hr>\n            <!-- end row -->\n\n')
        __M_writer('\n          </div>\n\n          <div class="rentals">\n')
        for rental in rentals:
            __M_writer('\n            ')

            total  += rental.rental_price
                        
            
            __M_writer('\n\n            <!-- row -->\n  \t\t\t\t\t<div class="row">\n  \t\t\t\t\t\t<div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\n  \t\t\t\t\t\t</div>\n  \t\t\t\t\t\t<div class="col-xs-4">\n  \t\t\t\t\t\t\t<h4 class="product-name"><strong>')
            __M_writer(str( rental.name ))
            __M_writer('</strong></h4><h4><small>')
            __M_writer(str( rental.description))
            __M_writer('</small></h4>\n  \t\t\t\t\t\t</div>\n  \t\t\t\t\t\t<div class="col-xs-6">\n  \t\t\t\t\t\t\t<div class="col-xs-6 text-right">\n  \t\t\t\t\t\t\t\t<h6><strong>')
            __M_writer(str( rental.rental_price ))
            __M_writer('<span class="text-muted">x</span></strong></h6>\n  \t\t\t\t\t\t\t</div>\n  \t\t\t\t\t\t\t<div class="col-xs-4">\n                  <h6><strong>1<span class="text-muted"></span></span></strong></h6>\n  \t\t\t\t\t\t\t</div>\n  \t\t\t\t\t\t</div>\n  \t\t\t\t\t</div>\n  \t\t\t\t\t<hr>\n            <!-- end row -->\n\n')
        __M_writer('\n          </div>\n\n\n\n          <!-- shipping and billing informaiton -->\n\n          <div class="row">\n\t\t\t\t\t\t<div class="col-xs-4 col-xs-offset-2">\n\t\t\t\t\t\t\t<h4><strong>Shipping</strong></h4><h4><small></small></h4>\n              <p>')
        __M_writer(str( request.user.first_name + ' ' + request.user.last_name ))
        __M_writer('<p>\n              <p>')
        __M_writer(str( address.street ))
        __M_writer('<p>\n              <p>')
        __M_writer(str( address.city + ', ' + address.state ))
        __M_writer('<p>\n              <p>')
        __M_writer(str( address.zip_code ))
        __M_writer('<p>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="col-xs-4">\n              <h4><strong>Details</strong></h4><h4><small></small></h4>\n              <p>Tracking number: #12382378468739</p>\n              <p>Ship Date: </p>\n              <p>Estimated Delivery Date: </p>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<hr>\n\n\n\t\t\t\t</div>\n\t\t\t\t<div class="panel-footer">\n\t\t\t\t\t<div class="row text-center">\n\t\t\t\t\t\t<div class="col-xs-9">\n\t\t\t\t\t\t\t<h4 class="text-right">Total <strong>')
        __M_writer(str( round(total,2) ))
        __M_writer('</strong></h4>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="col-xs-3">\n\t\t\t\t\t\t\t<a href="/shop/" class="btn btn-success btn-block">\n\t\t\t\t\t\t\t\tReturn\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <!-- no header -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"131": 3, "137": 131, "27": 0, "41": 1, "46": 7, "51": 136, "57": 9, "68": 9, "69": 26, "75": 30, "76": 33, "77": 34, "78": 35, "86": 41, "87": 48, "88": 48, "89": 48, "90": 48, "91": 52, "92": 52, "93": 55, "94": 55, "95": 63, "96": 67, "97": 68, "98": 69, "102": 71, "103": 78, "104": 78, "105": 78, "106": 78, "107": 82, "108": 82, "109": 93, "110": 103, "111": 103, "112": 104, "113": 104, "114": 105, "115": 105, "116": 106, "117": 106, "118": 122, "119": 122, "125": 3}, "source_encoding": "ascii", "uri": "email_receipt.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/email_receipt.html"}
__M_END_METADATA
"""
