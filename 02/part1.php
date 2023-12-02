<?php
if (count($argv) < 2) {
	echo "Please provide data file as argument";
	exit(1);
}
$data = array_filter(explode("\n", file_get_contents($argv[1])));
$colour_max = ["red" => 12, "green" => 13, "blue" => 14];

$total = 0;
foreach($data as $line) {
	[$p1, $rest] = explode(":", $line);
	[$game, $gameNumber] = explode(" ", $p1);
	$sets = explode(";", $rest);
	foreach($sets as $set) {
		$items = explode(",", $set);
		foreach($items as $item) {
			[$space, $num, $colour] = explode(" ", $item);
			if ($num > $colour_max[$colour]) {
				continue 3;
			}
		}
	}
	$total = $total + $gameNumber;
}
var_dump($total);
