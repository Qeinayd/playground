<?php

# https://www.codewars.com/kata/persistent-bugger/

function persistence(int $num): int {
  $count = 0;
  while($num > 9) {
    $num = array_product(str_split($num));
    $count++;
  }
  return $count;
}

?>
