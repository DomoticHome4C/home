<?php

$username="test";
$password="raspberry";
$database="temp_database";
  
$con=mysqli_connect(localhost,$username,$password, $database);
  
$query="SELECT * FROM tempLog";
$result=mysqli_query($con,$query);
  
$num=mysqli_num_rows($result);

function mysqli_result($res,$row=0,$col=0){ 
  $numrows = mysqli_num_rows($res); 
  if ($numrows && $row <= ($numrows-1) && $row >=0){ 
    mysqli_data_seek($res,$row); 
    $resrow = (is_numeric($col)) ? mysqli_fetch_row($res) : mysqli_fetch_assoc($res); 
    if (isset($resrow[$col])){ 
      return $resrow[$col]; 
      } 
  } 
  return false; 
}    

mysqli_close($con);
  
$tempValues = array();
  
$i=0;
while ($i < $num){
        $dateAndTemps = array();
        $datetime = mysqli_result($result,$i,"datetime");
        $temp = mysqli_result($result,$i,"temperature");
        
        $dateAndTemps["Date"] = $datetime;
        $dateAndTemps["Temp"] = $temp;
        $tempValues[$i]=$dateAndTemps;
        $i++;   
}
echo json_encode($tempValues);    
?>
