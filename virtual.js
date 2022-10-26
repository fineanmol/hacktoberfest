<HTML>
    <HEAD>

        <SCRIPT type="text/javascript" src="vkboard.js"></SCRIPT>

        <SCRIPT>

        // Minimal callback function:
        function keyb_callback(char)
        {
            // Let's bind vkeyboard to the <TEXTAREA>

            // with id="textfield":
            var text =
                document.getElementById("textfield"), val = text.value;

            switch(ch)
            {
                case "BackSpace":
                var min=(val.charCodeAt(val.length - 1) == 10) ? 2 : 1;
                text.value = val.substr(0, val.length - min);
                break;

               case "Enter":
                   text.value += "\n";
                   break;

               default:
                   text.value += ch;
            }
        }

        </SCRIPT>

    </HEAD>
    ...