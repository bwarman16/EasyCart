const searchForm = document.querySelector("form");
const searchResultDiv = document.querySelector(".search-result");
const container = document.querySelector(".container");

const APP_KEY = "9cdb20e752c35334803ea32fb835272f";
const APP_ID = "b62af782";

let searchQuery = "";

searchForm.addEventListener( 'submit', (e) => {
	e.preventDefault();
	searchQuery = e.target.querySelector('input').value;
	fetchAPI();
})

async function fetchAPI() {
	const baseURL = `https://api.edamam.com/search?q=${searchQuery}&app_id=${APP_ID}&app_key=${APP_KEY}`;
	const response = await fetch( baseURL );
	const data = await response.json();
	generateHTML( data.hits );
}

function generateHTML( results ) {
	let newHTML = '';

	results.map( result => {
		
		newHTML +=
		`
		<div class="item">
			<img src="${result.recipe.image}" alt="Food Image">
			<div class="flex-container">
				<h1 class="title">${result.recipe.label}</h1>
				<a class="view-button" href="${result.recipe.url}" target="_blank">View recipe</a>
			</div>
		</div>
		`
	})
	searchResultDiv.innerHTML = newHTML;
}
