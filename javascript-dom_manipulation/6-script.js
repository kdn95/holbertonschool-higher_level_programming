// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// 
// The name must be displayed in the HTML tag with id character.
// You must use the Fetch API.
// You probably should read something about using Promises later.
// 
// let character = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    return response.json();
  })
  .then((json) => {
    // console.log(json);
    character.textContent = json.name;
  })
  .catch((err) => console.error(`Fetch problem: ${err.message}`));