$(document).ready(function(){
    $(".sidebar-btn").click(function(){
      $(".wrapper").toggleClass("collapsee");
    });

    $('.nav_btn').click(function(){
      $('.mobile_nav_items').toggleClass('active');
    });

    $('#postformm').submit(function(event){
      event.preventDefault()
      var formData = $(this).serialize();
      console.log(formData)
      console.log('uhszk')
      
          $.ajax({
            url:$(this).attr("data-url"),
            type:'POST',
            data:formData,
            dataType:'json',
            success: function(data){
                $('.error').remove();
                console.log(response)
                if(response.error){
                    $.each(response.errors, function(name, error){
                        error = '<small class="text-muted error">' + error + '</small>'
                        $form.find('[name=' + name + ']').after(error);
                    })
                }
                else{
                    alert(response.message)
                    window.location = ""
                }
              }
            })
        //  clear the form.
      //   console('success')
      //   $("#postform").trigger('reset');
      //   alert(data.success);
      // },
      // error: function(message){
      //     alert('ERROR')
      // }
    // END of Ajax method
    }) // End of submit event
  
  }) // End of document ready function