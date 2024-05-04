/* Fetches and lists all movies title */
$(document).ready(function () {
  $.get('https://swapi.co/api/films/?format=json', (data) => {
    for (const film of data.results) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    }
  });
});
