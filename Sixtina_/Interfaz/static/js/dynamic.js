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
function abrirBoxLogin(){
  document.getElementById("box-login").style.display = "block";
}
function cerrarVentanas(){
  document.getElementById("box-login").style.display = "none";
  document.getElementById("box").style.display = "none";
  document.getElementById("boxNewAcount").style.display = "none"
}
function abrirBoxNew(){
  document.getElementById("box-login").style.display = "none";
  document.getElementById("boxNewAcount").style.display = "block";
}
