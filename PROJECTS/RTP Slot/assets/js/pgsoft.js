var x = [0, 974, 905, 873, 973, 852, 977, 966, 861, 882, 854, 929, 917, 885, 926, 941, 901, 927, 968, 853, 972, 860, 978, 855, 969, 919, 936, 979, 938, 898, 922, 877, 960, 918, 907, 970, 851, 947, 908, 935, 883, 856, 959, 896, 858, 913, 864, 893, 897, 872, 961, 876, 884, 930, 921, 912, 967, 931, 963, 910, 916, 976, 880, 920, 886, 902, 951, 889, 881, 850, 949, 866, 906, 909, 925, 890, 928, 932, 874929, 917, 885, 926, 941, 901, 927, 968, 853, 972, 860, 978, 855, 969, 919, 936];

for (let i = 1; i < 500; i++) {
    const d = new Date();
    var date = d.getUTCDate();
    var day = d.getUTCDay() + 1;
    var year = d.getUTCFullYear();
    var month = d.getUTCMonth() + 1;
    var hour = d.getUTCHours();
    var min = d.getMinutes();

    if (min < 30) {
        min = 1;
    } else {
        min = 2;
    }

    var xx = day + year * month * date;
    xx = Math.pow(xx, hour * min);
    xx = xx * x[i];

    if (i == 16 || i == 22 || i == 2 || i == 1 || i == 8 || i == 11 || i == 19 || i == 14 || i == 18 || i == 32 || i == 62 || i == 30 || i == 10 || i == 3 || i == 13 || i == 22 || i == 37) {
        xx = xx % 27;
        xx += 65;
    } else {
        xx = xx % 83;
        xx += 8;
    }

    $("#percent-txt-" + i).html(xx + "%");
    $("#percent-bar-" + i).attr("aria-valuenow", xx).css("width", xx + "%");

    if (xx < 30) {
        $("#percent-bar-" + i).addClass("red");
    } else if (xx > 70) {
        $("#percent-bar-" + i).addClass("green");
    } else {
        $("#percent-bar-" + i).addClass("yellow");
    }
}