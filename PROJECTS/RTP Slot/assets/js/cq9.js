var x = [0, 879, 280, 1513, 923, 1578, 2123, 994, 184, 2686, 2298, 2576, 228, 329, 2023, 2204, 2873, 1128, 117, 216, 1958, 2353, 1715, 2151, 199, 375, 2542, 764, 1963, 2582, 1803, 2885, 2086, 648, 629, 2817, 1927, 999, 380, 2871, 1932, 2068, 215, 2569, 1445, 1032, 1059, 329, 1887, 2449, 2004, 2099, 882, 974, 651, 2524, 1837, 334, 289, 961, 713, 342, 2860, 1298, 1947, 1450, 1927, 896, 1733, 1559, 1678, 1629, 535, 2702, 2323, 2851, 2666, 1891, 978, 976, 1342, 350, 1292, 1417, 261, 329, 2402, 1797, 2063, 1828, 2704, 2963, 1783, 22, 141, 925, 1038, 2181, 1375, 111, 990, 2112, 2876, 1979, 2049, 2682, 598, 2687, 1364, 2753, 1199, 2090, 598, 1480, 2158, 1226, 45, 682, 2600, 2106, 1964, 553, 658, 2882, 2405, 1262, 382, 1983, 901, 1777, 197, 1981, 1256, 1098, 2076, 1178, 2595, 1537, 273, 1500, 1921, 2820, 1008, 2926, 1079, 527, 105, 1047, 2940, 721, 2748, 1595, 1459, 1940, 1048, 687, 1420, 2589, 960, 2767, 2842, 373, 1104, 1490, 1309, 1615, 950, 792, 355, 1835, 676, 1643, 2242, 178, 1637, 1284, 2810, 2611, 1126, 791, 561, 2646, 1223, 2025, 2302, 2927, 26, 881, 186, 2116, 1427, 581, 2836, 1610, 1368, 15, 2676, 342, 116, 240, 418, 880, 550, 2394, 1376, 1268, 1191, 2044, 1645, 1356, 236, 2834, 2275, 384, 1345, 1164, 2308, 1184, 535, 288, 280, 2611, 1206, 2578, 2618, 633, 2055, 1162, 2029, 1846, 2827, 1175, 1400, 2711, 1504, 2499, 889, 2650, 182, 2863, 1737, 2425, 2012, 713, 2900, 2912, 305, 1090, 197, 1352, 776, 733, 727, 426, 1898, 2453, 2294, 2551, 178, 398, 1559, 816, 2982, 335, 518, 338, 634, 1558, 31, 4, 1993, 2708, 2143, 684, 750, 2891, 699, 94, 471, 1965, 449, 2342, 2508, 967, 998, 2569, 2439, 1214, 335, 983, 1620, 952, 908, 292, 114, 1535, 2818, 2039, 2291, 937, 1496];

for (let i = 1; i < 300; i++) {
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

    if (i == 44 || i == 35 || i == 48 || i == 74 || i == 105 || i == 41 || i == 69) {
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