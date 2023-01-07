// add all the javascript code here
var toggle = document.getElementById("toggle");
var container = document.getElementById("container");

toggle.onclick = function(){
	container.classList.toggle('active');
}
