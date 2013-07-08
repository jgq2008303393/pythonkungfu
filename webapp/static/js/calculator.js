console.log("Welcome to Calculator");
$('form').submit(function(evt) {
    evt.preventDefault();
    $.ajax({
        type: "POST",
        url: "",
        data: $('form').serialize(),
        success: function(data) {
            $('#hasil').html(data);
        }
    });
    return false;
});
