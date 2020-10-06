var click = localStorage.getItem("click");

function abrirBox(){
  document.getElementById("box").style.display = "block";
}
function cerrarBox(){
  document.getElementById("box").style.display = "none";
}
function mantenerBox(){
  document.getElementById("box").style.display = "block";
}
function abrirBox2(){
  document.getElementById("lista2").style.display = "block";
}
function cerrarBox2(){
  document.getElementById("lista2").style.display = "none";
}
function mantenerBox2(){
  document.getElementById("lista2").style.display = "block";
}
function cambiarPropiedades(id_click){
  document.getElementById(id_click.id).fontWeight = click;
  localStorage.setItem("click", click)
}
