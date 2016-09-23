$(function(){
     
 $('.selectpicker').selectpicker({
      style: 'btn-info',
      size: 4
  });

    $('#dynamic_select').on('change', function (){
        var url = $(this).val();
        if (url){
        window.location = '?q=' + url
        }
        return false;
  }); 
  $('#dynamic_select2').on('change', function (){
        var url = $(this).val();
        if (url){
        window.location = '?q=' + url
        }
        return false;
  });     

});