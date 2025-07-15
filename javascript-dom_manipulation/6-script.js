#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      document.getElementById('character').textContent = data.name;
    })
    .catch(error => {
      console.error('Error al obtener datos:', error);
      document.getElementById('character').textContent = 'Error al cargar personaje';
    });
});
