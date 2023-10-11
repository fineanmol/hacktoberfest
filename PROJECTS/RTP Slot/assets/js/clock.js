function GetClock(elm){
    var tzOffset = +7,
        d  = new Date(),
        dx = d.toGMTString(),
        dx = dx.substr(0,dx.length -3);
    
    d.setTime(Date.parse(dx))
    d.setHours(d.getHours()+tzOffset);

    var nday   = d.getDay(),
        nmonth = d.getMonth(),
        ndate  = d.getDate(),
        nyear  = d.getYear(),
        nhour  = d.getHours(),
        nmin   = d.getMinutes(),
        nsec   = d.getSeconds(), ap;
    var months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
    
    if (nhour == 0){ ap = " AM"; nhour = 12; }
    else if (nhour< 12){ ap = " AM"; }
    else if (nhour == 12){ ap = " PM"; }
    else if (nhour > 12){ ap = " PM"; nhour -= 12; }

    if (nyear < 1000) nyear += 1900;
    if (nmin <= 9) nmin = "0" + nmin;
    if (nsec <= 9) nsec = "0" + nsec;

    document.getElementById(elm).innerHTML = ndate + " " + months[nmonth] + " " + nyear + "&ensp;" + nhour + ":" + nmin + ":" + nsec + ap + "";
}

$(document).ready(function() {
    GetClock('jam');
    setInterval(function() { GetClock('jam'); },1000);
});