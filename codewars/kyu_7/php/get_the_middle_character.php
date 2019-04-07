<?php

# https://www.codewars.com/kata/get-the-middle-character/

function getMiddle($text) {
    $pivot = intdiv(strlen($text), 2);
    if (strlen($text) % 2) {
        return substr($text, $pivot, 1);
    }
    return substr($text, $pivot - 1, 2);
}

?>
