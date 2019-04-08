<?php

# https://www.codewars.com/kata/duplicate-encoder/

function duplicate_encode($word) {
    $result = "";
    $chars = str_split(strtolower($word));
    foreach ($chars as $char) {
        if (array_count_values($chars)[$char] == 1) {
            $result .= '(';
        } else {
            $result .= ')';
        }
    }
    return $result;
}

?>
