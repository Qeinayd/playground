<?php

# https://www.codewars.com/kata/remove-string-spaces/

function no_space(string $s): string {
    return preg_replace('/\s+/', '', $s);
}

?>
