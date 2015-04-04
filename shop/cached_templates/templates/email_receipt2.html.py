# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428102175.288158
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/email_receipt2.html'
_template_uri = 'email_receipt2.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\n\n<head>\n    <title>Order Receipt</title>\n</head>\n\n<body>\n\n    <h1>Thank You</h1>\n\n    <h2>Order Summary</h2>\n\n        <div class="items">\n\t\t\t<table>\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>Name</td>\n\t\t\t\t\t\t<td>Description</td>\n\t\t\t\t\t\t<td>Price</td>\n\t\t\t\t\t\t<td>Qty</td>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n')
        for key,value in items.items():
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n\t\t\t\t\t\t<td>')
            __M_writer(str( value[0].description ))
            __M_writer('</td>\n\t\t\t\t\t\t<td>')
            __M_writer(str( value[0].current_price ))
            __M_writer('</td>\n\t\t\t\t\t\t<td>')
            __M_writer(str( value[1] ))
            __M_writer('</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('\t\t\t\t</tbody>\n\t\t\t</table>\n        </div>\n\n')
        if rentals:
            __M_writer('\n\t\t')
            __M_writer(str( rentals ))
            __M_writer('\n\n        <h3>Rentals</h3>\n\n\t\t<div class="rentals">\n\t\t\t<table>\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>Name</td>\n\t\t\t\t\t\t<td>Description</td>\n\t\t\t\t\t\t<td>Price</td>\n\t\t\t\t\t\t<td>Qty</td>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n')
            for rental in rentals:
                __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>')
                __M_writer(str( rental.name ))
                __M_writer('</td>\n\t\t\t\t\t\t<td>')
                __M_writer(str( rental.description ))
                __M_writer('</td>\n\t\t\t\t\t\t<td>')
                __M_writer(str( rental.rental_price   ))
                __M_writer('</td>\n\t\t\t\t\t</tr>\n')
            __M_writer('\t\t\t\t</tbody>\n\t\t\t</table>\n        </div>\n\n')
        __M_writer('\n\t\t<h3>Total: ')
        __M_writer(str( total ))
        __M_writer('</h3>\n\n</body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "24": 1, "25": 24, "26": 25, "27": 26, "28": 26, "29": 27, "30": 27, "31": 28, "32": 28, "33": 29, "34": 29, "35": 32, "36": 36, "37": 37, "38": 38, "39": 38, "40": 53, "41": 54, "42": 55, "43": 55, "44": 56, "45": 56, "46": 57, "47": 57, "48": 60, "49": 65, "50": 66, "51": 66, "57": 51}, "uri": "email_receipt2.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/shop/templates/email_receipt2.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
