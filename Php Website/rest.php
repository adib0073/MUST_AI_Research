<?php 
 
 $base_url= 'https://en.wikipedia.org/w/api.php?action=opensearch&search=';
 $extended_url = '&limit=1&namespace=0&format=json';
 $keyword='Bill%20Gates';
 $wiki_url= $base_url.$keyword.$extended_url;
 //$data=file_get_contents('https://en.wikipedia.org/w/api.php?action=opensearch&search=Bill%20Gates&limit=1&namespace=0&format=json');
 $data=file_get_contents($wiki_url);
 $val=explode(",[\"",$data);
 $new_summary = $val[2];
 echo rtrim($new_summary,"\"]");
?>