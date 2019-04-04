<?php

# https://www.codewars.com/kata/sum-of-positive/

function positive_sum($arr) {
    $total = 0;
    
    foreach($arr as $number)
    {
      if($number > 0)
        $total += $number;
    }
    
    return $total;
}

?>
