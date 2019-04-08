<?php

# https://www.codewars.com/kata/multiples-of-3-or-5/

function solution($number){
    $result = array();
    for ($i = 0; $i < $number; $i++) {
        if (($i % 3 == 0) || ($i % 5) == 0) {
            array_push($result, $i);
        }
    }
    return array_sum($result);
}

?>
