<html>
<body>
<?php
$url = $_POST["url"];
echo nl2br("\n\nThe url you specified is:<b>$url<b>");
$python = 'C:\\Users\\aaygupta\\AppData\\Local\\Continuum\\anaconda3\\pythonw.exe';
$pyscript = 'test_edgedetection.py';
$cmd = "$python $pyscript $url";
exec("$cmd", $output);
//$source =  array('c:\\temp\\Source1.jpg','c:\\temp\\Source2.jpg','c:\\temp\\Source3.jpg');
//$result = array('c:\\temp\\final_result1.png','c:\\temp\\final_result2.png','c:\\temp\\final_result3.png');
$source = 'c:\\temp\\Source.jpg';
$result = 'c:\\temp\\final_result.png';
if (file_exists($source))
{
    echo nl2br("\n\nSource:\n\n");
    $imageData = base64_encode(file_get_contents($source));
    // Format the image SRC:  data:{mime};base64,{data};
    $src = 'data: '.mime_content_type($source).';base64,'.$imageData;
    // Echo out a sample image
    echo '<img src="' . $src . '">';
}
else
{
    echo "<b>Please give a valid url<b>";
}
if (file_exists($result))
{
    echo nl2br("\n\nResult:\n\n");
    $imageData = base64_encode(file_get_contents($result));
    // Format the image SRC:  data:{mime};base64,{data};
    $src = 'data: '.mime_content_type($result).';base64,'.$imageData;
    // Echo out a sample image
    echo '<img src="' . $src . '">';
}
else
{
    echo "<b>An error occured<b>";
}

#echo implode("",$output);
echo nl2br("\n\n<b>Completed execution<b>");
?>
</body>
</html>