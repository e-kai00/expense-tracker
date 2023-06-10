$(document).ready(function() {

    // Initialize Materialize Elements

    function initMaterialize() {
        $('.sidenav').sidenav();
        $('.modal').modal();
        $('select').formSelect();
    }
    
    initMaterialize();
    

  });


// Get current year for the Cpyright
  $('#copyright').text(new Date().getFullYear());