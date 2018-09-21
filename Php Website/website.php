<!DOCTYPE html>
<html lang="en">
<head>
    <title>Website Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<?php
$keyword = $_POST["keyword"];
$search_term = ucwords($keyword);
$keyword = str_replace(" ", "%20", $keyword);
//echo nl2br("\n\nThe url you specified is:<b>$url<b>");
$python = 'C:\\Users\\adbhatt\\AppData\\Local\\Continuum\\anaconda3\\pythonw.exe';


$base_url= 'https://en.wikipedia.org/w/api.php?action=opensearch&search=';
$extended_url = '&limit=1&namespace=0&format=json';

$wiki_url= $base_url.$keyword.$extended_url;

//$data=file_get_contents('https://en.wikipedia.org/w/api.php?action=opensearch&search=Bill%20Gates&limit=1&namespace=0&format=json');
$data=file_get_contents($wiki_url);
$val=explode(",[\"",$data);
$new_summary = $val[2];
$new_summary = rtrim($new_summary,"\"]");

$pyscript = 'test_imagesearch.py';
$cmd = "$python $pyscript $keyword";
exec("$cmd", $output);

$html = '<div class="container-fluid">';
$rows = 1;
$columns = 3;
for($i = 0; $i<$rows; $i++)
{
    $html .= '<div class="row">'; // OPEN ROW
    for($j = 1; $j <= $columns ; $j++)
    {
        $html.= '<div class="col-sm-4 col-md-4 col-lg-4">';
        switch($j)
        {
            case 1:  
                $html .= '<center><p style= "text-align:center;vertical-align:middle"><font face="Comic Sans MS" color="#666666"><h2>'.$search_term.'</h2></font></p></center>';
                break;
            case 2:
                if (file_exists("final_result1.png"))
                {
                    $imageData = base64_encode(file_get_contents("final_result1.png"));
                    // Format the image SRC:  data:{mime};base64,{data};
                    $src = 'data: '.mime_content_type("final_result1.png").';base64,'.$imageData;
                    // Echo out a sample image
                    $html.= '<p><img src = "final_result1.png" style="height: 100%; width: 100%; object-fit: contain"></p>';
                } 
                
                break;
            case 3:
                //$html .= '<p style= "text-align:center ; vertical-align:middle"><h3>'.$summary.implode().'</h3></p>';                
                
                $html .= '<br> <p style= "text-align:justify ; vertical-align:middle"><font face="Comic Sans MS" color="#666666"><h4>'.$new_summary.'</h4></font></p>';                
                break;
        }
           
        $html .= '</div>'; //OPEN COLUMN
    }
    $html.= '</div>';
}
$html .= '</div>';
echo $html;
#unlink("summary.txt");
?>
</body>
</html>