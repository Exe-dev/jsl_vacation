$(function () {
    var dayoff = $('#id_day_off_type');
    var reason = $('#id_reason_type');
    var detail = $('#id_detail_type');
    var start_day = $('#id_start_day');
    var end_day = $('#id_end_day');

    // 事由の動的変更
    dayoff.on('change', function () {
        var val = $(this).val();
        var next = reason.val();

        responseAjax("dayoff", val, next);
    }).trigger('change');

    // 詳細の動的変更
    reason.on('change', function () {
        var val = $(this).val();
        var next = detail.val();

        responseAjax("reason", val, next);
    }).trigger('change');

    // 時間を指定される前に時間制限有給休暇を指定した時に開始日と終了日を同じ日付にする
    start_day.on('change', function(){
        if(reason.html().match("time_able")){
            end_day.val(start_day.val());
        }
    }).trigger('change');
});

function responseAjax(type, value, next) {
    if (value === '') value = '0';
    if (next  === '') next  = '0';

    // $.ajax()でサーバーに選ばれた内容を送信(GET)
    $.ajax({
        url: "/pulldown" + "/" + type + "/" + value + "/" + next,
        type: 'GET',
        success: function (data) {
            var detail = $('#id_detail_type');
            if (data.match("detail_able")) {
                detail.prop('disabled', false);
            } else {
                detail.children('option[value=""]').prop('selected', true);
                detail.prop('disabled', true);
            }

            if (type === "dayoff") {
                $('#id_reason_type').html(data);

                var time = $('#id_start_time, #id_end_time');
                var start_day = $('#id_start_day'), end_day = $('#id_end_day');
                if (data.match("time_able")) {  // 時間制限有給休暇の場合
                    end_day.prop('disabled', true);
                    end_day.val(start_day.val());
                    time.prop('disabled', false);
                } else {                        // 時間制限有給休暇以外の場合
                    end_day.prop('disabled', false);
                    time.children('option[value=""]').prop('selected', true);
                    time.prop('disabled',true);
                }
            } else if (type === "reason") {
                $('#id_detail_type').html(data);
            }
        },
        error: function (e) {
            console.log(e);
        }
    });
}