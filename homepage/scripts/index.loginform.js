$(function() {


  $('#id_username').addClass('form-control')
  $('#id_password').addClass('form-control')
  $('#id_username').prop('placeholder','Username')
  $('#id_password').prop('placeholder','Password')

  $('#loginform').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform


  $('#forgot_password').on('click', function(){


      $.loadmodal({

        url: '/homepage/index.forgot_password/',
        title: 'Forgot Password',
        width: '500px',

      }); // loadmodal


  })


}); // Ready
