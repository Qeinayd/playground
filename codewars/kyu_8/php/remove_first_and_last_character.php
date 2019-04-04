<?php

# https://www.codewars.com/kata/remove-first-and-last-character/

function remove_char(string $s): string {
    return substr($s, 1, -1);
}

?>
