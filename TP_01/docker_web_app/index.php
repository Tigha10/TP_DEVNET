<?php
function initMysqlConnection(){
$pdo = new PDO('mysql:host=XXXXX;dbname=XXXX', “USERNAME”, “PASSWORD”);
return $pdo;
}
function getDevices($pdo){
$query = $pdo->query("SQL QUERY TO BE COMPLETED.....");
return $query;
}
$pdo = initMysqlConnection();
$devices = getDevices($pdo);
foreach ($devices as $row) {
echo "-------------------------------------\n";
echo "device name : ".."<br/>\n";
echo "device ip : ".."<br/>\n";
echo "device vendor : ".."<br/>\n";
}
?>