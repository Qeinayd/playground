<?php

# https://www.codewars.com/kata/find-the-parity-outlier/

function find($integers) {
    $odds = array();
    $evens = array();
    foreach ($integers as $elem) {
        if ($elem % 2) {
            array_push($odds, $elem);
        }
        else {
            array_push($evens, $elem);
        }
    }
    return sizeof($odds) < sizeof($evens) ? $odds[0] : $evens[0];
}

?>
