<?php

# https://www.codewars.com/kata/array-dot-diff/

function arrayDiff($a, $b) {
    $result = array();
    foreach ($a as $elem) {
        if (!in_array($elem, $b)) {
            array_push($result, $elem);
        }
    }
    return $result;
}

?>
