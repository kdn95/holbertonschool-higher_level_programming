// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// 
// All movie titles must be list in the HTML ul element with id list_movies
// You must use the Fetch API.

let list_movies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    return response.json();
  })
  .then((json) => {
    // console.log(json);

    for (let movie of json.results)
    {
        // console.log(movie.title);
        let new_item = document.createElement("li");
        new_item.textContent = movie.title;
    
        list_movies.appendChild(new_item);
    }
  })
  .catch((err) => console.error(`Fetch problem: ${err.message}`));