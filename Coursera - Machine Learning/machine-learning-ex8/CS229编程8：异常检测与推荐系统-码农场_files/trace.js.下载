var links = window.document.getElementsByTagName('link');
$(links).each(function() {
    if($(this).attr('rel') == 'shortlink')
    {
        var id = $(this).attr('href').split('=')[1];
        $.post("http://" + window.location.host + "/wp-content/plugins/hankcs/trace.php", { p: id },
            function(data){
            });
    }
});