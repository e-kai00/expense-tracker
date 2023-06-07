$(document).ready(function() {

    // Initialize Materialize Elements

    function initMaterialize() {
        $('.sidenav').sidenav();
    }
    
    initMaterialize();
    

  });


// Get current year for the Cpyright
  $('#copyright').text(new Date().getFullYear());