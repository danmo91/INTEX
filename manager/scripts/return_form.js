$(function() {


  $('#returnform').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform

  $(".my-checkbox").bootstrapSwitch({

      size: 'small',


  }); // bootstrap switch

  $('.selectpicker').selectpicker();

}); // Ready
