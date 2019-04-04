<?php

# https://www.codewars.com/kata/even-or-odd/

function even_or_odd(int $n): string {
    if ($n % 2) {
        return 'Odd';
    }
    return 'Even';
}

?>
