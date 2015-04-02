$(function() {


  $('#show_overdue_rentals').on('click', function(){

    event.preventDefault()


    $.loadmodal({

      url:'/manager/rentals.overdue/',
      title: 'Overdue Rentals',
      width: '600px',
    }); // Loadmodal

  }); // Click


}); // Ready
