$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
});

function popMenu(){
	// alert("Clicked!")
	$("#popupMenu").toggleClass("show")
}

function rotateSignup() {
	$("#login").css("transform", "rotateY(-180deg)")
	$("#signup").removeClass("form-side--back");

}

function rotateLogin() {
	// $(".form-side--front").css("transform", "rotateY(-180deg)");
	$("#signup").addClass("form-side--back");
	$("#login").css("transform", "rotateY(-0)")
}