$(document).ready(function(){
    $(window).on("beforeunload", function(e) {
        $.ajax({
                url: "login",
                method: 'GET',
            })
    });
});
