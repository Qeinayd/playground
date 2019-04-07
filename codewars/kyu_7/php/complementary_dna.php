<?php

# https://www.codewars.com/kata/complementary-dna/

function DNA_strand($dna) {
    return strtr($dna, array('A' => 'T','T' => 'A','C' => 'G','G' => 'C'));
}

?>
