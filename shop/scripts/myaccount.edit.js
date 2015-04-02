$(function() {



  $('#editform').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform


}); // ready
