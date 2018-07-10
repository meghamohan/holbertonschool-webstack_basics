$.get('https://swapi.co/api/films?format=json', function (data) {
    for (let r of data['results']) {
      $('UL#list_movies').append('<li>'+r['title']+'</li>');
    }
});
