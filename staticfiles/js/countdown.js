function get_lefttime(tm) {
    var rsv_hours = parseInt(tm[0]) + 4;      
    var rsv_minutes = parseInt(tm[1]);
    var rsv_seconds = parseInt(tm[2]);
    var date = new Date();
    var cur_hours = date.getHours();
    var cur_minutes = date.getMinutes();
    var cur_seconds = date.getSeconds();
    var total_seconds = (rsv_hours - cur_hours) * 3600 + (rsv_minutes - cur_minutes) * 60 + (rsv_seconds - cur_seconds)
    return total_seconds;
}

function check_time(time) {
    if (time < 10)
        return '0' + String(time)
    else
        return String(time)
}

function show_time(sp, seconds) {
    hours = Math.floor(seconds / 3600);
    minutes = Math.floor((seconds % 3600) / 60);
    seconds = seconds % 60;
    hours = check_time(hours);
    minutes = check_time(minutes);
    seconds = check_time(seconds);
    time = hours + ':' + minutes + ':' + seconds;
    sp.innerHTML = time;
}

function countdown() {
    lpars = new Array();
    for(i = 0; i <= 30; i++) {
        lpars[i] = 'LPAR' + i;
        var sp = document.getElementById(lpars[i]);
        if(!sp)
            continue;
        tm = sp.getAttribute('value').split(':');
        seconds = get_lefttime(tm);
        if (seconds >= 0)
            show_time(sp, seconds);
        else
            window.location.reload(); 
    }
    window.setTimeout(function (){countdown();}, 500);
}
