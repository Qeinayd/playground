<?php

# https://www.codewars.com/kata/valid-parentheses/

function validBraces($braces) {
    $brackets = array(
        "(" => ")",
        "[" => "]",
        "{" => "}",
    );
    $stack = array();
    
    foreach (str_split(strtolower($braces)) as $char) {
        if (array_key_exists($char, $brackets)) {
            array_push($stack, $char);
        } else {
            if (sizeof($stack) > 0 && $brackets[array_slice($stack, -1)[0]] == $char) {
                array_pop($stack);
            } else {
                return false;
            }
        }
    }
    return sizeof($stack) == 0;
}

?>
