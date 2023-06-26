$(document).ready(function() {

    // Initialize Materialize Elements

    function initMaterialize() {
        $('.sidenav').sidenav();
        $('.modal').modal();      
        $('select').formSelect();
    }

        
    initMaterialize();


  setTimeout(function() {
    $('#flash-message').fadeOut();
  }, 3500);
  
  // Get current year for the Cpyright
  $('#copyright').text(new Date().getFullYear());    

});


// Chart.js plagin
const plugin = {
  id: 'emptyDoughnut',
  afterDraw(chart, args, options) {
    const {datasets} = chart.data;
    const {color, width, radiusDecrease} = options;
    let hasData = false;

    for (let i = 0; i < datasets.length; i += 1) {
      const dataset = datasets[i];
      hasData |= dataset.data.length > 0;
    }

    if (!hasData) {
      const {chartArea: {left, top, right, bottom}, ctx} = chart;
      const centerX = (left + right) / 2;
      const centerY = (top + bottom) / 2;
      const r = Math.min(right - left, bottom - top) / 2;

      ctx.beginPath();
      ctx.lineWidth = width || 2;
      ctx.strokeStyle = color || 'rgba(255, 128, 0, 0.5)';
      ctx.arc(centerX, centerY, (r - radiusDecrease || 0), 0, 2 * Math.PI);
      ctx.stroke();
    }
  }
};




