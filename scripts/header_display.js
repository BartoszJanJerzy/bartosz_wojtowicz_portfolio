var myHeader = $("#header");
$(document).on("scroll", function() {
  var y = window.scrollY;
  if (y >= $("#about-subpage").offset().top) {
    $("#header").show();
  } else {
    $("#header").hide();
  }
});
