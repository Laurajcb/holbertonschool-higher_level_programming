const $ = window.jQuery;
$.get('https://swapi-api.hbtn.io/api/films/?format=json').click(function (data) {
  for (const movies of data.results) {
    $('UL#list_movies').append(`<li>${movies.title}<li>`);
  }
});
