function openTask(taskName, from) {
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
    if(from == 'click'){
        event.currentTarget.className += " active";
    }


}




        function Redirect(id) {
            window.location.href="/learnings-acheivements/view-learning/" + id;
        }



        function Review(id) {
            window.location.href="/learnings-acheivements/learning/" + id;
        }



$(document).ready(function () {
    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }
    };
    var tab = getUrlParameter('tab');
    if(tab == 'learning'){
        openTask('Achievement', 'load');
        $('#id_all_learn_tab').addClass("active")
    }else if(tab=='mylearn'){
        openTask('Learning', 'load');
        $('#id_my_learn_tab').addClass("active")
        }

     else if(tab=='myreview'){
     openTask('Review', 'load');
     $('#"id_my_review_tab"').addClass("active")
     }

});

