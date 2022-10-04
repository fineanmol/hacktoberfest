<?php
$sentence = "Hello World !!";
$stripedSentence = str_replace(' ','-',$sentence);

$newString = '';

for ($i=0; $i < strlen($stripedSentence); $i++) {
    if(ord($stripedSentence[$i]) < 65 || ord($stripedSentence[$i]) > 122){
        if($stripedSentence[$i] != "-"){
            str_replace($stripedSentence[$i],'',$stripedSentence);
        } else {
            $newString .= $stripedSentence[$i];
        }
    } else {
        $newString .= $stripedSentence[$i];
    }
    
}
echo strtolower($newString);