/* Adds class red to HTML tag HEADER to (#FF0000) when DIV#red_header clicked */
$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('header').addClass('red');
  });
});
