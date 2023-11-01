let url = "https://pokeapi.co/api/v2/pokemon?limit=151";

function mostrarDatos(pokemon) {
  let pkmnName = document.getElementById("pkmnName");
  let pkmnImg = document.getElementById("pkmnImg");
  let pkmnDesc = document.getElementById("pkmnDesc");
  // Obtener datos de pokemon individual
  fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`)
    .then((response) => response.json())
    .then((datosPkmn) => {
      //Llamar a modal con datos del pokemon
    });
}

function ObtenerPokemon() {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      let lista_pokemon = document.getElementById("lista-pokemon");
      // Resultados del fetch
      let pkmnList = data.results;
      pkmnList.forEach((element) => {
        // Crear elemento en la lista
        let li = document.createElement("li");
        li.classList.add("list-group-item");

        // Render pokemon
        let pkmn = document.createElement("button");
        pkmn.classList.add("btn", "btn-primary");
        pkmn.addEventListener("click", () => {
          mostrarDatos(element.name);
        });
        pkmn.innerText = element.name;

        // Agregar elemento a la lista
        li.appendChild(pkmn);
        lista_pokemon.append(li);
      });
    });
}
