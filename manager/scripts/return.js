$(function() {

  $('#email_button').on('click', function(){

      console.log('clicked');


      // send email via ajax
      $.ajax({url: "/manager/return.send_email/", success: function(result){

          console.log('ajax happened')

          if(result == "1"){

              // notify
              $.notify({
                    // options
                    icon: 'glyphicon glyphicon-star',
                    title: '<strong>Overdue Emails:</strong>',
                    message: 'Sent',
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


          }
          else {
              // notify
              $.notify({
                    // options
                    icon: 'glyphicon glyphicon-star',
                    title: '<strong>Overdue Emails:</strong>',
                    message: 'Failed',
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
          }


      }}); // ajax

  }); // email_button



}); // Ready
