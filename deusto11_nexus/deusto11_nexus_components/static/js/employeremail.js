// GET
const SERVICE_URL="http://127.0.0.1:8000/nexus.com/apiallemployer/"
function loadData() {
  fetch(SERVICE_URL)
  .then((response) => response.json())
  .then((json) => {
      for (let element of json) {          
      var dates='<td>'+element.name+'</td> <td>'+element.email+'</td>'
      console.log(dates)
      document.getElementById("tablaemail3").insertRow(-1).innerHTML = dates

      }
  });
}
  loadData();

// POST
document.getElementById("formulario").addEventListener("submit", Crearobj)
function Crearobj(event) {
event.preventDefault()
   var form = new FormData(document.getElementById("formulario"))
 fetch("http://127.0.0.1:8000/nexus.com/apiallemails/", {
 method :'POST',
    body : form
        })
        .then(response => response.json())
        .then(json => console.log(json))
        var aviso = document.createTextNode("Se ha creado el email correctamente");

p.appendChild(aviso);
}

