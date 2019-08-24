console.log('initiated')

$(document).ready(function(){
    $('#generate_button').click(function(){
        $.ajax({
            url: '/generate', 
            data: {'text': $('#intext').val()},
            type: 'POST',
            success: function(response) {
                $('#outtext').val(response);
            },
            error: function(error) {
                $('#outtext').val(error);
            }
        })
    })
})