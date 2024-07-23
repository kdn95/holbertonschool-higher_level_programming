// Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.
// 
// The translation of “hello” must be displayed in the HTML element with id hello
// Your script must work when it is imported from the <head> tag

window.onload = () => {
  let hello = document.getElementById("hello");

  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
  
      return response.json();
    })
    .then((json) => {
      hello.textContent = json.hello;
    })
    .catch((err) => console.error(`Fetch problem: ${err.message}`));
}