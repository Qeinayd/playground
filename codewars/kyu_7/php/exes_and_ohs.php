<?php

# https://www.codewars.com/kata/exes-and-ohs/

function XO($s) {
    $s = strtolower($s);
    return substr_count($s, 'x') == substr_count($s, 'o');
}

?>
