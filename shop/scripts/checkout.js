$(function() {

  $('#id_address1').addClass('form-control')
  $('#id_address2').addClass('form-control')
  $('#id_city').addClass('form-control')
  $('#id_state').addClass('form-control')
  $('#id_zip_code').addClass('form-control')
  $('#id_creditcard').addClass('form-control')
  $('#id_expiration').addClass('form-control')
  $('#id_csv').addClass('form-control')


  $('#id_address1').prop('placeholder','Street 1')
  $('#id_address2').prop('placeholder','Street 2')
  $('#id_city').prop('placeholder','City')
  $('#id_zip_code').prop('placeholder','Zip')
  $('#id_creditcard').prop('placeholder','Credit Card Number')
  $('#id_expiration').prop('placeholder','Card Expiration Date')
  $('#id_csv').prop('placeholder','CSV Number')

}); // ready
