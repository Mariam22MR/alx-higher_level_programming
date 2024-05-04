/* Adds LI element to a list when DIV#add_item clicked */
$(document).ready(function () {
	$('DIV#add_item').on('click', function () {
	  $('UL.my_list').append('<li>Item</li>')
	});
  });
