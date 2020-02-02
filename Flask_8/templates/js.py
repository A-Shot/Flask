$.ajax({
  url: "/press_",
  type: 'POST',
  data: data.serialize(),
  success: function(data){
   $("p").text(data);
  }
     });
