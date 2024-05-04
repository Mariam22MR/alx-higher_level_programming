/* Updates text of HEADER tag when user clicks DIV#update_header */
$(document).ready(function () {
	$('DIV#update_header').on('click', function () {
	  $('header').text('New Header!!!')
	});
  });
