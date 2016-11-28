/**
 * Created by shepherd on 16-11-28.
 */
$(function () {
    var url = '/';
    var page = 1;
    var scroll_flag = 1;
    $(window).scroll(function () {
        var args = {'page': page};
        if ($(document).height() - $(this).scrollTop() - $(this).height() < 1 && scroll_flag == 1) {
            $.post(url, args, function (data) {
                if (data) {
                    $("tbody").append(data);
                    page++;
                } else {
                    scroll_flag = 0;
                    return false;
                }
            });
        }
    });
});

