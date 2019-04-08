<?php

# https://www.codewars.com/kata/bit-counting/

function countBits($n) {
    return array_count_values(str_split(decbin($n)))["1"];
}

?>
