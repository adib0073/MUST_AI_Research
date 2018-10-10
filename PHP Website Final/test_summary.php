<?php
/*
$python = 'C:\\Users\\aaygupta\\AppData\\Local\\Continuum\\anaconda3\\pythonw.exe';
$pyscript = 'get_wikipedia_summary.py';
$keyword = 'Bill Gates';
$cmd = "$python $pyscript $keyword";
$proc = popen($cmd , 'r');
exec("$cmd", $summary);
echo "Reached eof";
*/
echo exec("C:\\Users\\aaygupta\\AppData\\Local\\Continuum\\anaconda3\\pythonw.exe get_wikipedia_summary.py");
//$myfile = fopen("summary.txt", "r") or die("Unable to open file!");
//$summary =  fread($myfile,filesize("summary.txt"));
?>