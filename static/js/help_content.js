function openTask(taskName) {
  // Declare all variables
  var i, tabcontent, tablinks;
  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("nav-link");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", " ");

  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(taskName).style.display = "block";
  event.currentTarget.className += " active";

}




$(window).scroll(function(e){
  var $el = $('.fixedElement');
  var isPositionFixed = ($el.css('position') == 'fixed');
  if ($(this).scrollTop() > 200 && !isPositionFixed){
    $el.css({'position': 'fixed', 'top': '0px'});
  }
  if ($(this).scrollTop() < 200 && isPositionFixed){
    $el.css({'position': 'static', 'top': '0px'});
  }
});


   function Redirect(id) {
               window.location.href="/learnings-acheivements/view-learning/"+id;
               }




function Review(id) {
               window.location.href="/learnings-acheivements/learning/"+id;
               }

