(function($) {$().ready(function() {
    
    function splitQueryString(s) {
        var r = {};        
        var q = s.substring(s.indexOf('?') + 1); // remove everything up to the ?
        q = q.replace(/\&$/, ''); // remove a trailing &
        $.each(q.split('&'), function() {
            var p = this.split('=');
            r[p[0]] = p[1];
        });
        return r;
    };
    
    $('#plone-contentmenu-workflow dd.actionMenuContent a[href*=content_status_modify]').each(function() {
         $(this).click(function() {
            var comment = prompt("Please enter a comment for this state change.");
            if(comment != null) {
                var href = $(this).attr('href');
                var baseHref = href.substring(0, href.indexOf('?'));
                var params = splitQueryString(href);
                params['comment'] = $.trim(comment);
                window.location.href = baseHref + '?' + $.param(params);
            }
            return false;
         });
    });

});})(jQuery);