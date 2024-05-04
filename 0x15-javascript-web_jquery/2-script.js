/* Update colour of HTML header to (#FF0000) tag DIV #red_header is clicked */
$(document).ready(function () {
  $('#red_header').on('click', function () {
    $('header').css('color', '#FF0000');
  });
});
