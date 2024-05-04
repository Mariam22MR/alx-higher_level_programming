/* Fetches and replaces name of URL */
$(document).ready(function () {
  $.get('https://swapi.co/api/people/5/?format=json', (data) => {
    $('DIV#character').text(data.name);
  });
});
