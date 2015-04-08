$(function() {

  // notify- welcome to homepage
  $.notify({

    // options
    icon: 'glyphicon glyphicon-star',
    title: '<strong>Welcome</strong>',
    message: 'to the Colonial Heritage Foundation',

  },{

    // settings
    offset: {
      x: 50,
      y: 75,
    },
    animate: {
      enter: 'animated fadeInRight',
      exit: 'animated fadeOutRight'
    },
    delay: 2500,

  }); // notify


  // modal to view overdue rentals
  $('#show_overdue_rentals').on('click', function(){

    event.preventDefault()
    $.loadmodal({

      url:'/manager/rentals.overdue/',
      title: 'Overdue Rentals',
      width: '600px',
    }); // Loadmodal

  }); // Click


}); // Ready
