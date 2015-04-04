$(function() {


    $('#data-table').DataTable();

  // overdue rentals
  $('#show_overdue_rentals').on('click', function(){

    event.preventDefault();


    $.loadmodal({

      url:'/manager/rentals.overdue/',
      title: 'Overdue Rentals',
      width: '600px',
    }); // Loadmodal

  }); // Click

  // Rental Return

  $('.return').on('click', function(){

      console.log('clicked')

      event.preventDefault();

      id = $(this).attr('data-id');
      console.log('id:', id)

      $.loadmodal({
          url:'/manager/return.return_form/' + id,
          title:'Return',
          width: '600px',
      }); //Loadmodal


  }); // click

  $('#returnform').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform





}); // Ready
