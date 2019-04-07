<?php

# https://www.codewars.com/kata/highest-and-lowest/

function highAndLow($numbers) {
    $numbers = array_map('intval', explode(' ', $numbers));
    return max($numbers) . ' ' . min($numbers);
}

?>
