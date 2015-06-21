$(document).ready( function() {

  /*
    Hack for showing correct tab in modal
  */
  $('#Register').on("click", function() {
    $('#qn-register').addClass("active fade in");
    $('#qn-login').removeClass("active");
  });

  /*
    Counter hack for showing correct tab in modal on access
  */
  $('.accedi').on("click", function() {
    $('#qn-register').removeClass("active fade in");
    $('#qn-login').addClass("active fade in");
  });


});
