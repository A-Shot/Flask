$(document).ready( function(){
  $("#button1").on("click", function( event ){
   let data_out = $("form").serializeArray();
      $.ajax({
        data: data_out,
        type: "POST",
        url: "/Get_New_Project"
      }).done(function(data) {
      $("#PROJECT_NUMBER").text(data.result);
   });
       event.preventDefault();
   });
 });

  
