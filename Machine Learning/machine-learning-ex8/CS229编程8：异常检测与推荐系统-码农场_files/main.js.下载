if( !window.console ){
    window.console = {
        log: function(){}
    }
}


/* 
 * jsui
 * ====================================================
*/
jsui.bd = $('body')
jsui.is_signin = jsui.bd.hasClass('logged-in') ? true : false;

if( $('.widget-nav').length ){
    $('.widget-nav li').each(function(e){
        $(this).hover(function(){
            $(this).addClass('active').siblings().removeClass('active')
            $('.widget-navcontent .item:eq('+e+')').addClass('active').siblings().removeClass('active')
        })
    })
}

if( $('.sns-wechat').length ){
    $('.sns-wechat').on('click', function(){
        var _this = $(this)
        if( !$('#modal-wechat').length ){
            $('body').append('\
                <div class="modal fade" id="modal-wechat" tabindex="-1" role="dialog" aria-hidden="true">\
                    <div class="modal-dialog" style="margin-top:200px;width:340px;">\
                        <div class="modal-content">\
                            <div class="modal-header">\
                                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
                                <h4 class="modal-title">'+ _this.attr('title') +'</h4>\
                            </div>\
                            <div class="modal-body" style="text-align:center">\
                                <img style="max-width:100%" src="'+ _this.data('src') +'">\
                            </div>\
                        </div>\
                    </div>\
                </div>\
            ')
        }
        $('#modal-wechat').modal()
    })
}


if( $('.carousel').length ){
    var el_carousel = $('.carousel')

    el_carousel.carousel({
        interval: 4000
    })

    require(['hammer'], function(Hammer) {

        // window.Hammer = Hammer
        
        var mc = new Hammer(el_carousel[0]);

        mc.on("panleft panright swipeleft swiperight", function(ev) {
            if( ev.type == 'swipeleft' || ev.type == 'panleft' ){
                el_carousel.carousel('next')
            }else if( ev.type == 'swiperight' || ev.type == 'panright' ){
                el_carousel.carousel('prev')
            }
        });

    })
}


if( Number(jsui.ajaxpager) > 0 && ($('.excerpt').length || $('.excerpt-minic').length) ){
    require(['ias'], function() {
        if( !jsui.bd.hasClass('site-minicat') && $('.excerpt').length ){
            $.ias({
                triggerPageThreshold: jsui.ajaxpager?Number(jsui.ajaxpager)+1:5,
                history: false,
                container : '.content',
                item: '.excerpt',
                pagination: '.pagination',
                next: '.next-page a',
                loader: '<div class="pagination-loading"><img src="'+jsui.uri+'/img/loading.gif"></div>',
                trigger: 'More',
                onRenderComplete: function() {
                    require(['lazyload'], function() {
                        $('.excerpt .thumb').lazyload({
                            data_attribute: 'src',
                            placeholder: jsui.uri + '/img/thumbnail.png',
                            threshold: 400
                        });
                    });
                }
            });
        }

        if( jsui.bd.hasClass('site-minicat') && $('.excerpt-minic').length ){
            $.ias({
                triggerPageThreshold: jsui.ajaxpager?Number(jsui.ajaxpager)+1:5,
                history: false,
                container : '.content',
                item: '.excerpt-minic',
                pagination: '.pagination',
                next: '.next-page a',
                loader: '<div class="pagination-loading"><img src="'+jsui.uri+'/img/loading.gif"></div>',
                trigger: 'More',
                onRenderComplete: function() {
                    require(['lazyload'], function() {
                        $('.excerpt .thumb').lazyload({
                            data_attribute: 'src',
                            placeholder: jsui.uri + '/img/thumbnail.png',
                            threshold: 400
                        });
                    });
                }
            });
        }
    });
}


/* 
 * lazyload
 * ====================================================
*/
if ( $('.thumb:first').data('src') || $('.widget_ui_posts .thumb:first').data('src') || $('.wp-smiley:first').data('src') || $('.avatar:first').data('src')) {
    require(['lazyload'], function() {
        $('.avatar').lazyload({
            data_attribute: 'src',
            placeholder: jsui.uri + '/img/avatar-default.png',
            threshold: 400
        })

        $('.widget .avatar').lazyload({
            data_attribute: 'src',
            placeholder: jsui.uri + '/img/avatar-default.png',
            threshold: 400
        })

        $('.thumb').lazyload({
            data_attribute: 'src',
            placeholder: jsui.uri + '/img/thumbnail.png',
            threshold: 400
        })

        $('.widget_ui_posts .thumb').lazyload({
            data_attribute: 'src',
            placeholder: jsui.uri + '/img/thumbnail.png',
            threshold: 400
        })

        $('.wp-smiley').lazyload({
            data_attribute: 'src',
            // placeholder: jsui.uri + '/img/thumbnail.png',
            threshold: 400
        })
    })
}


/* 
 * prettyprint
 * ====================================================
*/
$('pre').each(function(){
    if( !$(this).attr('style') ) $(this).addClass('prettyprint').addClass('prettyprint linenums');
});

if( $('.prettyprint').length ){
    require(['prettyprint'], function(prettyprint) {
        prettyPrint()
    })
};


/**
 * TOC
 */

if($(".post_nav").size())
{
    (function($, window, document, undefined){

        // our plugin constructor
        var OnePageNav = function(elem, options){
            this.elem = elem;
            this.$elem = $(elem);
            this.options = options;
            this.metadata = this.$elem.data('plugin-options');
            this.$win = $(window);
            this.sections = {};
            this.didScroll = false;
            this.$doc = $(document);
            this.docHeight = this.$doc.height();
        };

        // the plugin prototype
        OnePageNav.prototype = {
            defaults: {
                navItems: 'a',
                currentClass: 'current',
                changeHash: false,
                easing: 'swing',
                filter: '',
                scrollSpeed: 750,
                scrollThreshold: 0.5,
                begin: false,
                end: false,
                scrollChange: false
            },

            init: function() {
                // Introduce defaults that can be extended either
                // globally or using an object literal.
                this.config = $.extend({}, this.defaults, this.options, this.metadata);

                this.$nav = this.$elem.find(this.config.navItems);

                //Filter any links out of the nav
                if(this.config.filter !== '') {
                    this.$nav = this.$nav.filter(this.config.filter);
                }

                //Handle clicks on the nav
                this.$nav.on('click.onePageNav', $.proxy(this.handleClick, this));

                //Get the section positions
                this.getPositions();

                //Handle scroll changes
                this.bindInterval();

                //Update the positions on resize too
                this.$win.on('resize.onePageNav', $.proxy(this.getPositions, this));

                return this;
            },

            adjustNav: function(self, $parent) {
                self.$elem.find('.' + self.config.currentClass).removeClass(self.config.currentClass);
                $parent.addClass(self.config.currentClass);
            },

            bindInterval: function() {
                var self = this;
                var docHeight;

                self.$win.on('scroll.onePageNav', function() {
                    self.didScroll = true;
                });

                self.t = setInterval(function() {
                    docHeight = self.$doc.height();

                    //If it was scrolled
                    if(self.didScroll) {
                        self.didScroll = false;
                        self.scrollChange();
                    }

                    //If the document height changes
                    if(docHeight !== self.docHeight) {
                        self.docHeight = docHeight;
                        self.getPositions();
                    }
                }, 250);
            },

            getHash: function($link) {
                return $link.attr('href').split('#')[1];
            },

            getPositions: function() {
                var self = this;
                var linkHref;
                var topPos;
                var $target;

                self.$nav.each(function() {
                    linkHref = self.getHash($(this));
                    $target = $('#' + linkHref);

                    if($target.length) {
                        topPos = $target.offset().top;
                        self.sections[linkHref] = Math.round(topPos);
                    }
                });
            },

            getSection: function(windowPos) {
                var returnValue = null;
                var windowHeight = Math.round(this.$win.height() * this.config.scrollThreshold);

                for(var section in this.sections) {
                    if((this.sections[section] - windowHeight) < windowPos) {
                        returnValue = section;
                    }
                }

                return returnValue;
            },

            handleClick: function(e) {
                var self = this;
                var $link = $(e.currentTarget);
                var $parent = $link.parent();
                var newLoc = '#' + self.getHash($link);

                if(!$parent.hasClass(self.config.currentClass)) {
                    //Start callback
                    if(self.config.begin) {
                        self.config.begin();
                    }

                    //Change the highlighted nav item
                    self.adjustNav(self, $parent);

                    //Removing the auto-adjust on scroll
                    self.unbindInterval();

                    //Scroll to the correct position
                    self.scrollTo(newLoc, function() {
                        //Do we need to change the hash?
                        if(self.config.changeHash) {
                            window.location.hash = newLoc;
                        }

                        //Add the auto-adjust on scroll back in
                        self.bindInterval();

                        //End callback
                        if(self.config.end) {
                            self.config.end();
                        }
                    });
                }

                e.preventDefault();
            },

            scrollChange: function() {
                var windowTop = this.$win.scrollTop();
                var position = this.getSection(windowTop);
                var $parent;

                //If the position is set
                if(position !== null) {
                    $parent = this.$elem.find('a[href$="#' + position + '"]').parent();

                    //If it's not already the current section
                    if(!$parent.hasClass(this.config.currentClass)) {
                        //Change the highlighted nav item
                        this.adjustNav(this, $parent);

                        //If there is a scrollChange callback
                        if(this.config.scrollChange) {
                            this.config.scrollChange($parent);
                        }
                    }
                }
            },

            scrollTo: function(target, callback) {
                var offset = $(target).offset().top;

                $('html, body').animate({
                    scrollTop: offset
                }, this.config.scrollSpeed, this.config.easing, callback);
            },

            unbindInterval: function() {
                clearInterval(this.t);
                this.$win.unbind('scroll.onePageNav');
            }
        };

        OnePageNav.defaults = OnePageNav.prototype.defaults;

        $.fn.onePageNav = function(options) {
            return this.each(function() {
                new OnePageNav(this, options).init();
            });
        };

    })( jQuery, window , document );

//取得cookie
    function getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');    //把cookie分割成组
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];                      //取得字符串
            while (c.charAt(0)==' ') {          //判断一下字符串有没有前导空格
                c = c.substring(1,c.length);      //有的话，从第二位开始取
            }
            if (c.indexOf(nameEQ) == 0) {       //如果含有我们要的name
                return unescape(c.substring(nameEQ.length,c.length));    //解码并截取我们要值
            }
        }
        return false;
    }
//设置cookie
    function setCookie(name, value, seconds) {
        seconds = seconds || 0;   //seconds有值就直接赋值，没有为0
        var expires = "";
        if (seconds != 0 ) {      //设置cookie生存时间
            var date = new Date();
            date.setTime(date.getTime()+(seconds*1000));
            expires = "; expires="+date.toGMTString();
        }
        document.cookie = name+"="+escape(value)+expires+"; path=/";   //转码并赋值
    }

// 目录相关
    $(".post_nav_content").onePageNav({
        currentClass: "active",
        changeHash: false,
        filter: ":not(.external)",
        scrollSpeed: 800,
        scrollOffset: 0,
        scrollThreshold: 0.1,
        begin: false,
        end: false,
        scrollChange: false
    });

    function close_toc()
    {
        if($(".post_nav").is(':animated'))
        {
            return;
        }
        setCookie('post_nav_enable', '0', 31536000);
        if($(".post_nav").css("left") != "auto")
        {
            $(".post_nav").animate({width: "0"});
            $('.post_nav_close').animate({opacity:"0"}).hide();
        }
        else
        {
            $(".post_nav").animate({right:"-165px"});
        }
        $("#toc_label").text("打开目录");
    }

    function open_toc()
    {
        if($(".post_nav").is(':animated'))
        {
            return;
        }
        setCookie('post_nav_enable', '1', 31536000);
        if($(".post_nav").css("left") != "auto")
        {
            $(".post_nav").animate({width: "175px"});
            $('.post_nav_close').show().animate({opacity:"1"});
        }
        else
        {
            $(".post_nav").animate({right:$(window).width() <= 767 ? 2 : 20 + "px",opacity:"1"});
        }
        $("#toc_label").text("关闭目录");
    }

    function on_click_toc_button()
    {
        if (getCookie('post_nav_enable') === '0')
        {
            open_toc();
        }
        else
        {
            close_toc();
        }
    }

    $('.post_nav_close').click(function(){
        on_click_toc_button();
    });

    $('.post_nav_content').on('click', function(e){
        if(getCookie('post_nav_enable') === '0' || $(window).width() < 1660)
        {
            $('.post_nav_close').click();
        }
    });
    if(getCookie('post_nav_enable') === '0' || $(window).width() < 1660)
    {
        // 小屏人性化关闭
        close_toc();
    }
    $('.post_nav').mouseover(function() {
        if (getCookie('post_nav_enable') === '0')
        {
            open_toc();
        }
    });
    if ($(window).width() < 1660)
    {
        $('.post_nav').mouseleave(function(){
            if (getCookie('post_nav_enable') === '1')
                close_toc();
        });
    }
    $('.post_nav_top').click(function(){
        scrollTo();
    });
    $('.post_nav_bottom').click(function(){
        scrollTo('#respond');
        $('#comment').focus()
    });
}


/* 
 * rollbar
 * ====================================================
*/
jsui.rb_comment = '';
if (jsui.bd.hasClass('comment-open')) {
    jsui.rb_comment = "<li><a href=\"javascript:(scrollTo('#comments',-15));\"><i class=\"fa fa-comments\"></i></a><h6>去评论<i></i></h6></li>"
};

jsui.rb_toc = $(".post_nav").size() ? '<li><a href="javascript:(on_click_toc_button());"><i class="fa fa-list post_open_icon"></i></a><h6 id="toc_label">'
+ (getCookie('post_nav_enable') === '0' ? "打开目录" : "关闭目录")
+ '<i></i></h6></li>' : '';


jsui.bd.append('\
    <div class="m-mask"></div>\
    <div class="rollbar"><ul>'
    +'<li><a href="javascript:(scrollTo());"><i class="fa fa-angle-up"></i></a><h6>去顶部<i></i></h6></li>'
    +jsui.rb_toc
    +jsui.rb_comment
    +'</ul></div>\
')



var _wid = $(window).width()
video_ok()
$(window).resize(function(event) {
    _wid = $(window).width()
    video_ok()
});



var scroller = $('.rollbar')
var _fix = (jsui.bd.hasClass('nav_fixed') && !jsui.bd.hasClass('page-template-navs')) ? true : false
$(window).scroll(function() {
    var h = document.documentElement.scrollTop + document.body.scrollTop

    if( _fix && h > 0 && _wid > 720 ){
        jsui.bd.addClass('nav-fixed')
    }else{
        jsui.bd.removeClass('nav-fixed')
    }

    h > 200 ? scroller.fadeIn() : scroller.fadeOut();
})


/* 
 * bootstrap
 * ====================================================
*/
$('.user-welcome').tooltip({
    container: 'body',
    placement: 'bottom'
})



/* 
 * sign
 * ====================================================
*/
if (_wid>720 && !jsui.bd.hasClass('logged-in')) {
    require(['signpop'], function(signpop) {
        signpop.init()
    })
}


/* 
 * single
 * ====================================================
*/

var _sidebar = $('.sidebar')
if (_wid>1024 && _sidebar.length) {
    var h1 = 15,
        h2 = 30
    var rollFirst = _sidebar.find('.widget:eq(' + (jsui.roll[0] - 1) + ')')
    var sheight = rollFirst.height()

    rollFirst.on('affix-top.bs.affix', function() {
        rollFirst.css({
            top: 0
        })
        sheight = rollFirst.height()

        for (var i = 1; i < jsui.roll.length; i++) {
            var item = jsui.roll[i] - 1
            var current = _sidebar.find('.widget:eq(' + item + ')')
            current.removeClass('affix').css({
                top: 0
            })
        };
    })

    rollFirst.on('affix.bs.affix', function() {
        rollFirst.css({
            top: h1
        })

        for (var i = 1; i < jsui.roll.length; i++) {
            var item = jsui.roll[i] - 1
            var current = _sidebar.find('.widget:eq(' + item + ')')
            current.addClass('affix').css({
                top: sheight + h2
            })
            sheight += current.height() + 15
        };
    })

    rollFirst.affix({
        offset: {
            top: _sidebar.height(),
            bottom: $('.footer').outerHeight()
        }
    })


}







$('.plinks a').each(function(){
    var imgSrc = $(this).attr('href')+'/favicon.ico'
    $(this).prepend( '<img src="'+imgSrc+'">' )
})


/* 
 * comment
 * ====================================================
*/
if (jsui.bd.hasClass('comment-open')) {
    require(['comment'], function(comment) {
        comment.init()
    })
}


/* 
 * page u
 * ====================================================
*/
if (jsui.bd.hasClass('page-template-pagesuser-php')) {
    require(['user'], function(user) {
        user.init()
    })
}


/* 
 * page theme
 * ====================================================
*/
if (jsui.bd.hasClass('page-template-pagestheme-php')) {
    require(['theme'], function(theme) {
        theme.init()
    })
}


/* 
 * page nav
 * ====================================================
*/
if( jsui.bd.hasClass('page-template-pagesnavs-php') ){

    var titles = ''
    var i = 0
    $('#navs .items h2').each(function(){
        titles += '<li><a href="#'+i+'">'+$(this).text()+'</a></li>'
        i++
    })
    $('#navs nav ul').html( titles )

    $('#navs .items a').attr('target', '_blank')

    $('#navs nav ul').affix({
        offset: {
            top: $('#navs nav ul').offset().top,
            bottom: $('.footer').height() + $('.footer').css('padding-top').split('px')[0]*2
        }
    })


    if( location.hash ){
        var index = location.hash.split('#')[1]
        $('#navs nav li:eq('+index+')').addClass('active')
        $('#navs nav .item:eq('+index+')').addClass('active')
        scrollTo( '#navs .items .item:eq('+index+')' )
    }
    $('#navs nav a').each(function(e){
        $(this).click(function(){
            scrollTo( '#navs .items .item:eq('+$(this).parent().index()+')' )
            $(this).parent().addClass('active').siblings().removeClass('active')
        })
    })
}


/* 
 * page search
 * ====================================================
*/
if( jsui.bd.hasClass('search-results') ){
    var val = $('.site-search-form .search-input').val()
    var reg = eval('/'+val+'/i')
    $('.excerpt h2 a, .excerpt .note').each(function(){
        $(this).html( $(this).text().replace(reg, function(w){ return '<b>'+w+'</b>' }) )
    })
}


/* 
 * search
 * ====================================================
*/
$('.search-show').bind('click', function(){
    $(this).find('.fa').toggleClass('fa-remove')

    jsui.bd.toggleClass('search-on')

    if( jsui.bd.hasClass('search-on') ){
        $('.site-search').find('input').focus()
        jsui.bd.removeClass('m-nav-show')
    }
})

/* 
 * phone
 * ====================================================
*/

jsui.bd.append( $('.site-navbar').clone().attr('class', 'm-navbar') )

$('.m-icon-nav').on('click', function(){
    jsui.bd.addClass('m-nav-show')

    $('.m-mask').show()

    jsui.bd.removeClass('search-on')
    $('.search-show .fa').removeClass('fa-remove') 
})

$('.m-mask').on('click', function(){
    $(this).hide()
    jsui.bd.removeClass('m-nav-show')
})




if ($('.article-content').length){
    $('.article-content img').attr('data-tag', 'bdshare')
}

function video_ok(){
    $('.article-content embed, .article-content video, .article-content iframe').each(function(){
        var w = $(this).attr('width'),
            h = $(this).attr('height')
        if( h ){
            $(this).css('height', $(this).width()/(w/h))
        }
    })
}




/* 
 * baidushare
 * ====================================================
*/
if( $('.bdsharebuttonbox').length ){

    if ($('.article-content').length) $('.article-content img').data('tag', 'bdshare')

    window._bd_share_config = {
        common: {
            "bdText": '',
            "bdMini": "2",
            "bdMiniList": false,
            "bdPic": '',
            "bdStyle": "0",
            "bdSize": "24"
        },
        share: [{
            // "bdSize": 12,
            bdCustomStyle: jsui.uri + '/css/share.css'
        }]/*,
        slide : {    
            bdImg : 4,
            bdPos : "right",
            bdTop : 200
        },
        image: {
            tag: 'bdshare',
            "viewList": ["qzone", "tsina", "weixin", "tqq", "sqq", "renren", "douban"],
            "viewText": " ",
            "viewSize": "16"
        },
        selectShare : {
            "bdContainerClass":'article-content',
            "bdSelectMiniList":["qzone","tsina","tqq","renren","weixin"]
        }*/
    }

    with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?cdnversion='+~(-new Date()/36e5)];
}



/* functions
 * ====================================================
 */
function scrollTo(name, add, speed) {
    if (!speed) speed = 300
    if (!name) {
        $('html,body').animate({
            scrollTop: 0
        }, speed)
    } else {
        if ($(name).length > 0) {
            $('html,body').animate({
                scrollTop: $(name).offset().top + (add || 0)
            }, speed)
        }
    }
}


function is_name(str) {
    return /.{2,12}$/.test(str)
}
function is_url(str) {
    return /^((http|https)\:\/\/)([a-z0-9-]{1,}.)?[a-z0-9-]{2,}.([a-z0-9-]{1,}.)?[a-z0-9]{2,}$/.test(str)
}
function is_qq(str) {
    return /^[1-9]\d{4,13}$/.test(str)
}
function is_mail(str) {
    return /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/.test(str)
}


$.fn.serializeObject = function(){
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};


function strToDate(str, fmt) { //author: meizz   
    if( !fmt ) fmt = 'yyyy-MM-dd hh:mm:ss'
    str = new Date(str*1000)
    var o = {
        "M+": str.getMonth() + 1, //月份   
        "d+": str.getDate(), //日   
        "h+": str.getHours(), //小时   
        "m+": str.getMinutes(), //分   
        "s+": str.getSeconds(), //秒   
        "q+": Math.floor((str.getMonth() + 3) / 3), //季度   
        "S": str.getMilliseconds() //毫秒   
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (str.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}



