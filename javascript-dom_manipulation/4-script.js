// Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item:
// 
// The new element must be: <li>Item</li> The new element must be added to the ul element with class my_list

let add_item = document.getElementById("add_item");
let my_list = document.querySelector("ul.my_list");

add_item.onclick = addNewListItem;

function addNewListItem() {
    let new_item = document.createElement("li");
    new_item.textContent = "Item";

    my_list.appendChild(new_item);
}