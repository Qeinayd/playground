<?php

# https://www.codewars.com/kata/vowel-count/

function getCount($str) {
    return substr_count($str, 'a') +
        substr_count($str, 'e') +
        substr_count($str, 'i') +
        substr_count($str, 'o') +
        substr_count($str, 'u');
}

?>
