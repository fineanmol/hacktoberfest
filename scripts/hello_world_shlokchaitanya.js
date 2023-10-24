const d = 'hello world';
const abc = 'abcdefghijklmnopqrstuvwxyz';
var a = true;
var s = '';

for (var i = 0; i < d.length; i++) {
    for (var j = 0; a; j++) {
        if (abc[j] == undefined) {
            console.log(" "); 
            s = s + " ";

            break;
        }
        if (abc[j] == d[i] || abc[j] != d[i] ) {
            console.log(s + abc[j]);
            if (abc[j] == d[i]) {
                s = s + abc[j];
                break;
            }
        }
    }
}