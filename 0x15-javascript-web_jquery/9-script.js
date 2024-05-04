/* Fetches from URL and displays value of hello from fetch in DIV#hello */
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('DIV#hello').text(data.hello);
  });
});
