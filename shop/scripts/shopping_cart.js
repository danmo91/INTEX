$(function() {


  // Delete from cart

  $('.delete_from_cart').on('click', function() {

    console.log('delete clicked')

    var id = $(this).attr('data-id');
    var product = $(this).attr('data-product');

    console.log('product?:', product)

    $.loadmodal({

      url: '/shop/shopping_cart.delete/' + id + '/' + product,
      title: 'Shopping Cart',
      width: '800px',
      buttons: {
        "Checkout": function() {
          // do something here
          window.location.href = "/shop/checkout/";
          // a false return here cancels the automatic closing of the dialog
        },
      },
      onShow: function(dlg) {
        $('.button-panel').find('.btn').addClass('pull-right btn-warning')
        $('.button-panel').css({height: "60px"})
      },


    }); // loadmodal

  }); // click




}); // ready
