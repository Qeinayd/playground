<?php

# https://www.codewars.com/kata/find-the-odd-int/

function findIt(array $seq) : int {
    foreach ($seq as $elem) {
        if (count(array_keys($seq, $elem)) % 2 === 1) {
            return $elem;
        }
    }
}

?>
