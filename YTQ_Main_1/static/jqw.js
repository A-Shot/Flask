$(document).ready( function(){
 
   
 $("#MyForm").submit( function( event ){
   
   
   let data_out = $("#Form1").serializeArray();
  
   
   $.ajax({
     data: data_out,
     type: "POST",
     url: "/new_project_ajax"
   }).done(function(data) {
      
     
   });
   
   event.preventDefault();
   
   });    
});
